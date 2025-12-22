from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Avg
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import GameItem, Employee
from .serializers import GameItemSerializer, EmployeeSerializer


class GameItemViewSet(viewsets.ModelViewSet):
    queryset = GameItem.objects.all()
    serializer_class = GameItemSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


search_param = openapi.Parameter(
    'q', openapi.IN_QUERY, type=openapi.TYPE_STRING, description="Поиск по имени"
)

@swagger_auto_schema(method='get', manual_parameters=[search_param],
                     responses={200: EmployeeSerializer(many=True)})
@api_view(['GET'])
def employee_search(request):
    q = request.GET.get('q', '')
    employees = Employee.objects.filter(first_name__icontains=q)
    return Response(EmployeeSerializer(employees, many=True).data)


@swagger_auto_schema(method='get', responses={200: EmployeeSerializer(many=True)})
@api_view(['GET'])
def employees_by_position(request, position):
    employees = Employee.objects.filter(position__iexact=position)
    return Response(EmployeeSerializer(employees, many=True).data)


@swagger_auto_schema(method='get', responses={200: EmployeeSerializer(many=True)})
@api_view(['GET'])
def employees_by_experience(request, years):
    employees = Employee.objects.filter(experience_years__gte=years)
    return Response(EmployeeSerializer(employees, many=True).data)


@swagger_auto_schema(method='get', responses={200: openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "total_employees": openapi.Schema(type=openapi.TYPE_INTEGER),
        "average_salary": openapi.Schema(type=openapi.TYPE_NUMBER),
        "active_employees": openapi.Schema(type=openapi.TYPE_INTEGER),
    }
)})
@api_view(['GET'])
def employee_stats(request):
    return Response({
        "total_employees": Employee.objects.count(),
        "average_salary": Employee.objects.aggregate(Avg('salary'))['salary__avg'],
        "active_employees": Employee.objects.filter(is_active=True).count(),
    })
