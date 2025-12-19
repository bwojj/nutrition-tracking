from django.urls import path, include 
from rest_framework import routers 
from .views import DayView, MealView, FoodDataView

router = routers.DefaultRouter()
router.register(r"days", DayView, "day")
router.register(r"meals", MealView, "meal")
router.register(r"food-data", FoodDataView, "food-info")

urlpatterns = [
    path("api/", include(router.urls))
]