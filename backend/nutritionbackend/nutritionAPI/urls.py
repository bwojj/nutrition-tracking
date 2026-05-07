from django.urls import path, include 
from rest_framework import routers 
from .views import (
    DayView, MealView, FoodDataView, ProgressView, UserView, FoodsView, add_food,
    update_progress, CustomRefreshTokenView, CustomTokenObtainPairView,
    logout, register, is_authenticated, health_check, save_to_favorites, remove_from_favorites,
    add_to_saved_meals
    )

router = routers.DefaultRouter()
router.register(r"days", DayView, "day")
router.register(r"meals", MealView, "meal")
router.register(r"food-data", FoodDataView, "food-info")
router.register(r"progress", ProgressView, "progress-info")
router.register(r"user", UserView, "user-info")
router.register(r"foods", FoodsView, "foods")

urlpatterns = [
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', CustomRefreshTokenView.as_view(), name="token_refresh"),
    path("api/", include(router.urls)),
    path('api/add-food/', add_food, name='food-add'),
    path('api/update-progress/', update_progress, name="progress-update"),
    path('api/add-favorite/', save_to_favorites, name="add_to_favorites"), 
    path('api/remove-favorite/', remove_from_favorites, name="remove_from_favorites"), 
    path('api/add-saved-meal/', add_to_saved_meals, name="add_saved_meals"), 
    path('logout/', logout, name="logout"),
    path('authenticated/', is_authenticated, name="authenticated"),
    path('register/', register, name="register"),
    path('health/', health_check, name="health"),
]