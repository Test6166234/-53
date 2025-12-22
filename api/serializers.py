from rest_framework import serializers
from .models import GameItem, Employee

class GameItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameItem
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
