from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import health, ActivityViewSet, UserViewSet, LeaderboardViewSet, TeamViewSet, WorkoutViewSet

router = DefaultRouter()
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'users', UserViewSet, basename='user')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'workouts', WorkoutViewSet, basename='workout')

urlpatterns = [
    path('health/', health, name='health'),
    path('', include(router.urls)),
]
