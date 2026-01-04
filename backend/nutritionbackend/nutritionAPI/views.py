from datetime import date
from rest_framework import viewsets 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Day, Meal, FoodData, Progress
from django.contrib.auth.models import User
from .serializers import DaySerializer, MealSerializer, FoodDataSerializer, ProgressSerializer

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

class ProgressView(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

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
        fiber = request.data.get('fiber'),
        sugar = request.data.get('sugar'),
        saturated_fat = request.data.get('saturated_fat'),
        polyunsaturated_fat = request.data.get('polyunsaturated_fat'),
        monounsaturated_fat = request.data.get('monounsaturated_fat'),
        trans_fat = request.data.get('trans_fat'),
        cholesterol = request.data.get('cholesterol'),
        sodium = request.data.get('sodium'),
        potassium = request.data.get('potassium'),
        vitamin_A = request.data.get('vitamin_a'),
        vitamin_C = request.data.get('vitamin_c'),
        calcium = request.data.get('calcium'),
    )

    return Response({"status": "success", "message": f"Added {food.food_name} to {meal_obj.meal_name}"})

@api_view(['POST'])
def update_progress(request):
    user_profile = User.objects.first()

    progress_obj, _ = Progress.objects.update_or_create(
        user=user_profile,
        defaults={
            'goal_calories': request.data.get("goalCalories"),
            'goal_protein': request.data.get("goalProtein"),
            'goal_carbs': request.data.get("goalCarbs"),
            'goal_fat': request.data.get("goalFat"),
            'current_weight': request.data.get("currentWeight"),
            'goal_weight': request.data.get("goalWeight"),
            'goal': request.data.get("goal"),
        }
    )

    return Response({"status": "success", "message": f"Added {progress_obj}"})