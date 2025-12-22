from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GameItemViewSet,
    EmployeeViewSet,
    employee_search,
    employees_by_position,
    employees_by_experience,
    employee_stats,
)

router = DefaultRouter()
router.register('items', GameItemViewSet)
router.register('employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('employees/search/', employee_search, name="employee_search"),
    path('employees/position/<str:position>/', employees_by_position, name="employees_by_position"),
    path('employees/experience/<int:years>/', employees_by_experience, name="employees_by_experience"),
    path('employees/stats/', employee_stats, name="employee_stats"),
]
