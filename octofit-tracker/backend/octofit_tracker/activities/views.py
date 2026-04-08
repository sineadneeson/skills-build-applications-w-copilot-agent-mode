def health(request):
	return JsonResponse({'status': 'ok', 'service': 'octofit-backend'})

from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import Activity
from .serializers import ActivitySerializer, UserSerializer, LeaderboardSerializer, TeamSerializer, WorkoutSerializer

class ActivityViewSet(viewsets.ModelViewSet):
	queryset = Activity.objects.all()
	serializer_class = ActivitySerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer

# Stub viewsets for Leaderboard, Teams, Workouts
class LeaderboardViewSet(viewsets.ViewSet):
	def list(self, request):
		# Example static data
		data = [
			{"id": 1, "user": "alice", "score": 100},
			{"id": 2, "user": "bob", "score": 80},
		]
		return Response(data)

class TeamViewSet(viewsets.ViewSet):
	def list(self, request):
		data = [
			{"id": 1, "name": "Team Alpha"},
			{"id": 2, "name": "Team Beta"},
		]
		return Response(data)

class WorkoutViewSet(viewsets.ViewSet):
	def list(self, request):
		data = [
			{"id": 1, "name": "Pushups", "description": "Do 20 pushups"},
			{"id": 2, "name": "Squats", "description": "Do 30 squats"},
		]
		return Response(data)
