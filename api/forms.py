from django import forms
from .models import Car, Movie, GameItem, Employee

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'category', 'price', 'engine', 'top_speed', 'fuel_type', 'photo']

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'trailer_url', 'poster_url']

class GameItemForm(forms.ModelForm):
    class Meta:
        model = GameItem
        fields = ['name', 'type', 'power', 'level', 'description', 'rarity']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'position', 'salary', 'experience_years', 'is_active']
