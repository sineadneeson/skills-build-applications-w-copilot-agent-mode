from djongo import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Additional fields can be added here
    pass

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ArrayReferenceField(to=User, on_delete=models.CASCADE)

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    date = models.DateField(auto_now_add=True)

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
