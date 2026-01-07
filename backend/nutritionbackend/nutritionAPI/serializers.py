from rest_framework import serializers 
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import Day, Meal, FoodData, Progress

class RegisterSerializer(serializers.ModelSerializer):
    # Defines email field that the API will be getting
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    # Defines password field that the API will be getting 
    password = serializers.CharField(
        write_only=True, required=True, style={'input_type': 'password'}
    )

    # Defines the confim password field that the API will be getting 
    password_confirm = serializers.CharField(
        write_only=True, required=True, style={'input_type': 'password'}
    )

    # Shows how the serializer should work
    class Meta:
        # sets the model to be affected as user
        model = User

        # sets the fields to utilize in the model
        fields = ('username', 'password', 'password_confirm', 'email')

    # Makes sure the passwords match
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    # Creates the user model 
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
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