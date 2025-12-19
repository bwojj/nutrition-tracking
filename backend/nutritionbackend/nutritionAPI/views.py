from rest_framework import viewsets 
from .models import Day, Meal, FoodData
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
