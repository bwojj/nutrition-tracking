from datetime import date, timedelta
from django.utils import timezone
from rest_framework import viewsets 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Day, Meal, FoodData, Progress, Foods, SavedMeal
from django.contrib.auth.models import User
from .serializers import (DaySerializer, MealSerializer, FoodDataSerializer, 
        ProgressSerializer, UserRegistrationSerializer, UserSerializer, FoodsSerializer, SavedMealSerializer
        )

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

            res.data = {
                'success': True,
                'access': access_token,
                'refresh': refresh_token,
            }

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
            # Try cookie first (Chrome), fall back to request body (Safari)
            refresh_token = request.COOKIES.get('refresh_token') or request.data.get('refresh')

            if not refresh_token:
                return Response({"refreshed": False, "error": "No refresh token"})

            request.data['refresh'] = refresh_token

            response = super().post(request, *args, **kwargs)

            tokens = response.data 
            access_token = tokens['access']

            res = Response()

            res.data = {
                'refreshed': True,
                'access': access_token,
            }

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
            return Response({"refreshed": False})

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

class SavedMealView(viewsets.ModelViewSet): 
    serializer_class = SavedMealSerializer
    queryset = SavedMeal.objects.all()

class ProgressView(viewsets.ModelViewSet):
    serializer_class = ProgressSerializer
    def get_queryset(self):
        user_profile = self.request.user

        return Progress.objects.filter(user=user_profile)

class FoodsView(viewsets.ModelViewSet):
    queryset = Foods.objects.all()
    serializer_class = FoodsSerializer

    def list(self, request, *args, **kwargs):
        sort = request.query_params.get('sort', 'recent')

        if sort == 'id':
            queryset = Foods.objects.order_by('-id')
        elif sort == 'favorite':
            queryset = Foods.objects.order_by('-favorite').filter(favorite=True)
        else:
            queryset = Foods.objects.order_by('-date_last_used')
        search = request.query_params.get('search')
        if search:
            queryset = queryset.filter(food_name__icontains=search)
        id = request.query_params.get('id')
        if id:
            queryset = queryset.filter(id=id)
        queryset = queryset[:20]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    

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

    food_obj = Foods.objects.get(
        id=request.data.get("food_id")
    )

    food, _ = FoodData.objects.get_or_create(
        meal = meal_obj,
        food_from = food_obj, 
        food_name = request.data.get('food_name'),
        serving_size = request.data.get('serving_size') or '1 serving',
        calories = request.data.get('calories') or 0,
        protein = request.data.get('protein') or 0,
        carbs = request.data.get('carbs') or 0,
        fat = request.data.get('fat') or 0,
        fiber = request.data.get('fiber') or 0,
        sugar = request.data.get('sugar') or 0,
        saturated_fat = request.data.get('saturated_fat') or 0,
        polyunsaturated_fat = request.data.get('polyunsaturated_fat') or 0,
        monounsaturated_fat = request.data.get('monounsaturated_fat') or 0,
        trans_fat = request.data.get('trans_fat') or 0,
        cholesterol = request.data.get('cholesterol') or 0,
        sodium = request.data.get('sodium') or 0,
        potassium = request.data.get('potassium') or 0,
        vitamin_A = request.data.get('vitamin_a') or 0,
        vitamin_C = request.data.get('vitamin_c') or 0,
        calcium = request.data.get('calcium') or 0,
    )

    Foods.objects.filter(food_name=request.data.get('food_name')).update(date_last_used=timezone.now())

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

@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    return Response({'status': 'ok'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_to_favorites(request):
    try: 
        food_obj = Foods.objects.get(id=request.data.get('id'))
        food_obj.favorite = True;

        food_obj.save(update_fields=['favorite']) 

        return Response({'success': 'true'})
    except Exception as e: 
        return Response({'Error': f"{e}"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def remove_from_favorites(request):
    try: 
        food_obj = Foods.objects.get(id=request.data.get('id'))
        food_obj.favorite = False;

        food_obj.save(update_fields=['favorite']) 

        return Response({'success': 'true'})
    except Exception as e: 
        return Response({'Error': f"{e}"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_saved_meals(request):
    try:
        saved_meal_obj, _ = SavedMeal.objects.get_or_create(
            user=User.objects.first(), 
            meal_name=request.data.get("custom_meal_name")
        )

        food_objects = list()

        for i in request.data.get("ids"):
            food_obj = Foods.objects.get(
                id=i
            )
            food_objects.append(food_obj)

        for food in food_objects: 
            saved_meal_obj.foods.add(food)
        saved_meal_obj.save()

        return Response({'Success': True})
        
    except Exception as e:
        return Response({'Error': f"{e}"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_saved_meal_foods(request):
   try: 
        saved_meal_object = SavedMeal.objects.get(id=request.data.get("id"))

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

        res = Response({})

        for f in saved_meal_object.foods.all():
            food, _ = FoodData.objects.get_or_create(
                meal = meal_obj,
                food_name = f.food_name,
                serving_size = f.serving_size or '1 serving',
                calories = f.calories or 0,
                protein = f.protein or 0,
                carbs = f.carbs or 0,
                fat = f.fat or 0,
                fiber = f.fiber or 0,
                sugar = f.sugar or 0,
                saturated_fat = f.saturated_fat or 0,
                polyunsaturated_fat = f.polyunsaturated_fat or 0,
                monounsaturated_fat = f.monounsaturated_fat or 0,
                trans_fat = f.trans_fat or 0,
                cholesterol = f.cholesterol or 0,
                sodium = f.sodium or 0,
                potassium = f.potassium or 0,
                vitamin_A = f.vitamin_A or 0,
                vitamin_C = f.vitamin_C or 0,
                calcium = f.calcium or 0,
            )
            res.data[f"{f.food_name}"] = f"Added {f.food_name} to {meal_obj.meal_name}"

        return res
   except Exception as e:
       return Response({"Error": f"{e}"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_multiple_foods(request): 
    try: 
        foods_data = request.data.get("foods")

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

        for f in foods_data:
            FoodData.objects.create(
                meal = meal_obj,
                food_name = f.get('food_name'),
                serving_size = f.get('serving_size') or '1 serving',
                calories = f.get('calories') or 0,
                protein = f.get('protein') or 0,
                carbs = f.get('carbs') or 0,
                fat = f.get('fat') or 0,
                fiber = f.get('fiber') or 0,
                sugar = f.get('sugar') or 0,
                saturated_fat = f.get('saturated_fat') or 0,
                polyunsaturated_fat = f.get('polyunsaturated_fat') or 0,
                monounsaturated_fat = f.get('monounsaturated_fat') or 0,
                trans_fat = f.get('trans_fat') or 0,
                cholesterol = f.get('cholesterol') or 0,
                sodium = f.get('sodium') or 0,
                potassium = f.get('potassium') or 0,
                vitamin_A = f.get('vitamin_a') or 0,
                vitamin_C = f.get('vitamin_c') or 0,
                calcium = f.get('calcium') or 0,
            )

        return Response({'status': 'success'})
    
    except Exception as e:
        return Response({"Error": f"{e}"}) 


@api_view(["POST"])
@permission_classes([IsAuthenticated])
# receives food data object
def update_food_data(request):
    try: 
        food_data_obj = FoodData.objects.get(id=request.data.get("food_id"))

        food_derived_from = Foods.objects.get(id=food_data_obj.food_from.id)

        food_data_obj.calories = round(food_derived_from.calories * request.data.get("new_serving_size"))
        food_data_obj.protein = round(food_derived_from.protein * request.data.get("new_serving_size"))
        food_data_obj.carbs = round(food_derived_from.carbs * request.data.get("new_serving_size"))
        food_data_obj.fat = round(food_derived_from.fat * request.data.get("new_serving_size"))
        food_data_obj.fiber = round(food_derived_from.fiber * request.data.get("new_serving_size"))
        food_data_obj.sugar = round(food_derived_from.sugar * request.data.get("new_serving_size"))
        food_data_obj.saturated_fat = round(food_derived_from.saturated_fat * request.data.get("new_serving_size"))
        food_data_obj.polyunsaturated_fat = round(food_derived_from.polyunsaturated_fat * request.data.get("new_serving_size"))
        food_data_obj.monounsaturated_fat = round(food_derived_from.monounsaturated_fat * request.data.get("new_serving_size"))
        food_data_obj.trans_fat = round(food_derived_from.trans_fat * request.data.get("new_serving_size"))
        food_data_obj.cholesterol = round(food_derived_from.cholesterol * request.data.get("new_serving_size"))
        food_data_obj.sodium = round(food_derived_from.sodium * request.data.get("new_serving_size"))
        food_data_obj.potassium = round(food_derived_from.potassium * request.data.get("new_serving_size"))
        food_data_obj.vitamin_A = round(food_derived_from.vitamin_A * request.data.get("new_serving_size"))
        food_data_obj.vitamin_C = round(food_derived_from.vitamin_C * request.data.get("new_serving_size") )
        food_data_obj.calcium = round(food_derived_from.calcium * request.data.get("new_serving_size"))
        
        food_data_obj.save(update_fields=["serving_size", "calories", "protein", "carbs", "fat", "fiber", "sugar", "saturated_fat", 
                                          "polyunsaturated_fat", "monounsaturated_fat", "trans_fat", "cholesterol", "sodium", "potassium",
                                          "vitamin_A", "vitamin_C", "calcium"])

        return Response({"Success": f"{food_data_obj.food_name} serving size updated to {food_data_obj.serving_size}"})
    except Exception as e:
        return Response({"Error": f"{e}"})



       