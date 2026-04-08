from django.db import models
from django.conf import settings

class Activity(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	duration = models.PositiveIntegerField(help_text='Duration in minutes')

	def __str__(self):
		return f"{self.user.username} - {self.name} ({self.duration} min)"
