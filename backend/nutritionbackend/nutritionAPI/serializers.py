from rest_framework import serializers 
from .models import Day, Meal, FoodData, Progress

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'

class FoodDataSerializer(serializers.ModelSerializer):
    meal = serializers.SlugRelatedField(
        read_only=True,
        slug_field='meal_name'
     )
    class Meta:
        model = FoodData
        fields = '__all__'

class ProgressSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Progress 
        fields = '__all__'