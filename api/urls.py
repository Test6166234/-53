from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    home,
    movies_list,
    movie_create,  # Добавлен импорт представления для создания фильма
    tasks_list,
    task_create,
    gameitems_list,
    employees_list,
    employee_search,
    employees_by_position,
    employees_by_experience,
    employee_stats,
    GameItemViewSet,
    EmployeeViewSet,
    MovieViewSet,
    TaskViewSet,
    EmployeeStatsViewSet,
)

# ===== DRF ROUTER =====
router = DefaultRouter()
router.register("items", GameItemViewSet)
router.register("employees", EmployeeViewSet)
# router.register("movies", MovieViewSet)
router.register("tasks", TaskViewSet)
router.register("employee-stats", EmployeeStatsViewSet, basename="employee-stats")


urlpatterns = [
    # ===== САЙТ =====
    path("", home, name="home"),
    path("movies/", movies_list, name="movies_list"),
    path("movies/create/", movie_create, name="movie_create"),  # Добавлен маршрут для создания фильма
    path("tasks/", tasks_list, name="tasks_list"),
    path("tasks/create/", task_create, name="task_create"),
    path("gameitems/", gameitems_list, name="gameitems_list"),
    path("employees/", employees_list, name="employees_list"),

    # ===== API =====
    path("api/", include(router.urls)),
    path("api/employees/search/", employee_search, name="employee_search"),
    path(
        "api/employees/position/<str:position>/",
        employees_by_position,
        name="employees_by_position",
    ),
    path(
        "api/employees/experience/<int:years>/",
        employees_by_experience,
        name="employees_by_experience",
    ),
    path("api/employees/stats/", employee_stats, name="employee_stats"),
]
