from datetime import date, timedelta
from rest_framework import viewsets 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Day, Meal, FoodData, Progress
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .serializers import DaySerializer, MealSerializer, FoodDataSerializer, ProgressSerializer, RegisterSerializer

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer 

class DayView(viewsets.ModelViewSet):
    serializer_class = DaySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Day.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        user_profile = request.user
        today = date.today()

        for i in range(8):
            future_date = today + timedelta(days=i)
            Day.objects.get_or_create(user=user_profile, date=future_date)

        return super().list(request, *args, **kwargs)

class MealView(viewsets.ModelViewSet):
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Meal.objects.filter(day__user=self.request.user)

class FoodDataView(viewsets.ModelViewSet):
    serializer_class = FoodDataSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print("=== REQUEST USER ===", self.request.user, self.request.user.is_authenticated)
        queryset = FoodData.objects.filter(meal__date__user=self.request.user)
        date_param = self.request.query_params.get('date')
        if date_param:
            queryset = queryset.filter(meal__date__date=date_param)
        return queryset

class ProgressView(viewsets.ModelViewSet):
    serializer_class = ProgressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Progress.objects.filter(user=self.request.user)

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_food(request): 

    date_str = request.data.get('date')

    target_date = date_str if date_str else date.today()
    user_profile = request.user

    day_obj, _ = Day.objects.get_or_create(
        user=user_profile,
        date=target_date,
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

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_progress(request):
    user_profile = request.user

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