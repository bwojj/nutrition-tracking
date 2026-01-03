from django.contrib import admin
from .models import Day, Meal, FoodData, Progress

# Register your models here.

admin.site.register([Day, Meal, FoodData, Progress])