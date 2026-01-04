from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Day(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='days', default=1)
    date = models.DateField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'date'], name='unique_day_per_user')
        ]

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals', default=1)
    date = models.ForeignKey(Day, on_delete=models.CASCADE, related_name="meals")
    meal_name = models.CharField(max_length=64)

    class Meta:
        unique_together = ('user', 'date', 'meal_name')


class FoodData(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="item", default=1)
    food_name = models.CharField(max_length=64)
    calories = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()
    fiber = models.FloatField()
    sugar = models.FloatField()
    saturated_fat = models.FloatField()
    polyunsaturated_fat = models.FloatField()
    monounsaturated_fat = models.FloatField()
    trans_fat = models.FloatField()
    cholesterol = models.FloatField()
    sodium = models.FloatField()
    potassium = models.FloatField()
    vitamin_A = models.FloatField()
    vitamin_C = models.FloatField()
    calcium = models.FloatField()
    
class Progress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='goals', default=1)
    goal_calories = models.IntegerField()
    goal_protein =  models.IntegerField()
    goal_carbs =  models.IntegerField()
    goal_fat =  models.IntegerField()
    current_weight = models.FloatField()
    goal_weight = models.FloatField()
    goal = models.CharField(max_length=64)

