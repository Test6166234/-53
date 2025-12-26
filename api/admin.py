from django.contrib import admin
from .models import Task, TaskStep, GameItem, Employee


# ===== Inline шаги задачи =====
class TaskStepInline(admin.TabularInline):
    model = TaskStep
    extra = 1


# ===== Задачи (KANBAN) =====
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'user', 'created_at')
    list_filter = ('status', 'user')
    search_fields = ('title', 'description')
    inlines = [TaskStepInline]


# ===== Игровые предметы =====
@admin.register(GameItem)
class GameItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'item_type', 'power', 'level', 'rarity')
    list_filter = ('item_type', 'rarity')
    search_fields = ('name', 'description')


# ===== Сотрудники =====
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'position',
        'salary',
        'experience_years',
        'is_active'
    )
    list_filter = ('position', 'is_active')
    search_fields = ('first_name', 'last_name')
