from django.db import models

class GameItem(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    power = models.IntegerField()
    level = models.IntegerField()
    description = models.TextField()
    rarity = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    salary = models.IntegerField()
    experience_years = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
