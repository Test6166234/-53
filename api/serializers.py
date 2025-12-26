from rest_framework import serializers
from .models import GameItem, Employee, Movie, Task


class GameItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameItem
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
