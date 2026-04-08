from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']

# Stubs for Leaderboard, Teams, Workouts
class LeaderboardSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = serializers.CharField()
    score = serializers.IntegerField()

class TeamSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

class WorkoutSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()