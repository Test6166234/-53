from django.db import models
from django.contrib.auth.models import User


# ===== Машины =====
class Car(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    engine = models.CharField(max_length=50)
    top_speed = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="cars/", blank=True, null=True)

    def __str__(self):
        return self.name


# ===== Фильмы =====
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    trailer_url = models.URLField(blank=True, null=True)
    poster_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


# ===== Игровые предметы =====
class GameItem(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    power = models.IntegerField()
    level = models.IntegerField()
    description = models.TextField()
    rarity = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# ===== Сотрудники =====
class Employee(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    position = models.CharField(max_length=500)
    salary = models.IntegerField()
    experience_years = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# ===== KANBAN ЗАДАЧИ =====
class Task(models.Model):
    STATUS_CHOICES = [
        ("new", "Новая"),
        ("progress", "В процессе"),
        ("done", "Готово"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks",
        null=True,        # ← чтобы НЕ ПАДАЛО без логина
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# ===== Шаги задачи =====
class TaskStep(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="steps"
    )
    text = models.CharField(max_length=300)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.text
from django.db import models
from django.contrib.auth.models import User


# ===== Игровые предметы =====
class GameItem(models.Model):
    name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=50)
    rarity = models.CharField(max_length=50)
    power = models.IntegerField()
    level = models.IntegerField()
    quantity = models.IntegerField(default=1)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# ===== Сотрудники =====
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    salary = models.IntegerField()
    experience_years = models.IntegerField()
    hire_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# ===== Фильмы (оставлены только как сущность данных для API) =====
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    release_year = models.IntegerField()
    duration_minutes = models.IntegerField()
    rating = models.FloatField(default=0)
    director = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# ===== KANBAN ЗАДАЧИ =====
class Task(models.Model):
    STATUS_CHOICES = [
        ("new", "Новая"),
        ("progress", "В процессе"),
        ("done", "Готово"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    priority = models.IntegerField(default=1)
    estimated_hours = models.IntegerField(default=1)
    deadline = models.DateField(null=True, blank=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks",
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# ===== Шаги задачи =====
class TaskStep(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="steps"
    )
    text = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    order = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
