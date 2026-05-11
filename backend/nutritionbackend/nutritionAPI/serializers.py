from rest_framework import serializers 
from django.contrib.auth.models import User 
from .models import Day, Meal, FoodData, Progress, Foods, SavedMeal

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User 
        fields = ['username', 'email']

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta: 
        model=User 
        fields=['username', 'email', 'password']
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user 

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

class FoodsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Foods
        fields = '__all__'


class SavedMealSerializer(serializers.ModelSerializer):
    class Meta: 
        model = SavedMeal
        fields = '__all__'