from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Movie, Task, GameItem, Employee
from .serializers import MovieSerializer, TaskSerializer, GameItemSerializer, EmployeeSerializer


# ======================
# СТРАНИЦЫ
# ======================

def home(request):
    return render(request, "api/home.html")


def movies_list(request):
    # Получаем все фильмы
    movies = Movie.objects.all()
    return render(request, "api/movies_list.html", {"movies": movies})


def tasks_list(request):
    # Получаем задачи по статусам
    return render(
        request,
        "api/tasks_list.html",
        {
            "tasks_todo": Task.objects.filter(status="new"),
            "tasks_in_progress": Task.objects.filter(status="progress"),
            "tasks_done": Task.objects.filter(status="done"),
        }
    )


def gameitems_list(request):
    # Получаем все игровые предметы
    items = GameItem.objects.all()
    return render(request, "api/gameitems_list.html", {"items": items})


def employees_list(request):
    # Получаем всех сотрудников
    employees = Employee.objects.all()
    return render(request, "api/employees_list.html", {"employees": employees})


# ======================
# СОЗДАНИЕ ЗАДАЧИ
# ======================

def task_create(request):
    status = request.GET.get("status", "new")

    if request.method == "POST":
        # Проверка, если пользователь анонимный
        user = request.user if request.user.is_authenticated else None

        Task.objects.create(
            title=request.POST["title"],
            description=request.POST.get("description", ""),
            status=request.POST.get("status", status),
            user=user  # user может быть None для анонимных пользователей
        )
        return redirect("tasks_list")

    return render(request, "api/task_form.html", {"status": status})


# ======================
# СОЗДАНИЕ ФИЛЬМА
# ======================

def movie_create(request):
    # Логика для создания фильма
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title and description:
            # Создаем новый фильм
            Movie.objects.create(title=title, description=description)
            return redirect('movies_list')

        else:
            return render(request, 'movies/create_movie.html', {
                'error': 'Пожалуйста, заполните все поля.'
            })


    return render(request, 'api/movies/create_movie.html')


# ======================
# API (DRF)
# ======================

from rest_framework import viewsets

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class GameItemViewSet(viewsets.ModelViewSet):
    queryset = GameItem.objects.all()
    serializer_class = GameItemSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# ======================
# СТАТИСТИКА
# ======================

from rest_framework.response import Response

class EmployeeStatsViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response(
            Employee.objects
            .values("position")
            .annotate(total=Count("id"))
        )


# ======================
# ФИЛЬТРЫ
# ======================

def employee_search(request):
    q = request.GET.get("q", "")
    return render(
        request,
        "api/employees_list.html",
        {
            "employees": Employee.objects.filter(first_name__icontains=q)
        }
    )


def employees_by_position(request, position):
    return render(
        request,
        "api/employees_list.html",
        {
            "employees": Employee.objects.filter(position=position)
        }
    )


def employees_by_experience(request, years):
    return render(
        request,
        "api/employees_list.html",
        {
            "employees": Employee.objects.filter(experience_years__gte=years)
        }
    )


def employee_stats(request):
    return render(
        request,
        "api/employee_stats.html",
        {
            "stats": Employee.objects
            .values("position")
            .annotate(total=Count("id"))
        }
    )
