from datetime import date
from rest_framework import viewsets 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Day, Meal, FoodData
from django.contrib.auth.models import User
from .serializers import DaySerializer, MealSerializer, FoodDataSerializer

# Create your views here.

class DayView(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

class MealView(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class FoodDataView(viewsets.ModelViewSet):
    queryset = FoodData.objects.all()
    serializer_class = FoodDataSerializer

@api_view(['POST'])
def add_food(request): 
    today = date.today()

    user_profile = User.objects.first()

    day_obj, _ = Day.objects.get_or_create(
        user=user_profile,
        date=today
    )
    meal_obj, _ = Meal.objects.get_or_create(
        user=user_profile, 
        date=day_obj,
        meal_name=request.data.get('meal_name')
    )
    food, _ = FoodData.objects.get_or_create(
        meal = meal_obj, 
        food_name = request.data.get('food_name'),
        calories = request.data.get('calories'),
        protein = request.data.get('protein'),
        carbs = request.data.get('carbs'),
        fat =   request.data.get('fat'),
    )

    return Response({"status": "success", "message": f"Added {food.food_name} to {meal_obj.meal_name}"})

