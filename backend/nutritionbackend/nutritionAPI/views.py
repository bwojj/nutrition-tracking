from datetime import date, timedelta
from rest_framework import viewsets 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Day, Meal, FoodData, Progress
from django.contrib.auth.models import User
from .serializers import (DaySerializer, MealSerializer, FoodDataSerializer, 
        ProgressSerializer, UserRegistrationSerializer, UserSerializer)

from rest_framework.decorators import api_view, permission_classes 
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try: 
            response = super().post(request, *args, **kwargs)
            tokens = response.data 

            access_token = tokens['access']
            refresh_token = tokens['refresh']

            res = Response()

            res.data = {'success': True}

            res.set_cookie(
                key="access_token", 
                value=access_token, 
                httponly=True, 
                secure=True,
                samesite='None',
                path='/', 
            )
            res.set_cookie(
                key="refresh_token", 
                value=refresh_token, 
                httponly=True, 
                secure=True,
                samesite='None',
                path='/', 
            )
            return res
        except: 
            return Response({"success": False})

class CustomRefreshTokenView(TokenRefreshView): 
    def post(self, request, *args, **kwargs): 
        try: 
            refresh_token = request.COOKIES.get('refresh_token')

            request.data['refresh'] = refresh_token

            response = super().post(request, *args, **kwargs)

            tokens = response.data 
            access_token = tokens['access']

            res = Response()
            
            res.data = {'refreshed': True}

            res.set_cookie(
                key="access_token",
                value=access_token, 
                httponly=True,
                secure=True,
                samesite='None', 
                path="/",
            )

            return res
        except: 
            return Response({"success": False})

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user 

        return User.objects.filter(username=user)

class DayView(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

    def list(self, request, *args, **kwargs):
        # Logic to ensure next 7 days exist
        user_profile = User.objects.first()
        today = date.today()
        
        for i in range(8):  # Today + 7 days
            future_date = today + timedelta(days=i)
            Day.objects.get_or_create(user=user_profile, date=future_date)
            
        return super().list(request, *args, **kwargs)

class MealView(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class FoodDataView(viewsets.ModelViewSet):
    serializer_class = FoodDataSerializer

    def get_queryset(self):
        queryset = FoodData.objects.all()
        date_param = self.request.query_params.get('date')
        
        if date_param:
            queryset = queryset.filter(meal__date__date=date_param)
            
        return queryset

class ProgressView(viewsets.ModelViewSet):
    serializer_class = ProgressSerializer
    def get_queryset(self):
        user_profile = self.request.user

        return Progress.objects.filter(user=user_profile)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_food(request): 

    date_str = request.data.get('date')

    target_date = date_str if date_str else date.today()
    user_profile = User.objects.first()

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

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['POST'])
def logout(request):
    try:
        res = Response()
        res.data = {'success': True}
        res.delete_cookie('access_token', path="/", samesite='None')
        res.delete_cookie('refresh_token', path="/", samesite='None')

        return res
    except: 
        return Response({"success": False})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def is_authenticated(request): 
    return Response({'authenticated': True})
