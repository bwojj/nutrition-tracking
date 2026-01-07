from django.urls import path, include 
from rest_framework import routers 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import DayView, MealView, FoodDataView, ProgressView, RegisterView, add_food, update_progress

router = routers.DefaultRouter()
router.register(r"days", DayView, "day")
router.register(r"meals", MealView, "meal")
router.register(r"food-data", FoodDataView, "food-info")
router.register(r"progress", ProgressView, "progress-info")

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='auth_register'),
    path("api/", include(router.urls)),
    path('api/add-food/', add_food, name='food-add'),
    path('api/update-progress/', update_progress, name="progress-update")
]