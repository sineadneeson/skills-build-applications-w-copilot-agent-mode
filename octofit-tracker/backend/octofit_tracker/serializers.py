from rest_framework import serializers
from bson import ObjectId

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)
    def to_internal_value(self, data):
        return ObjectId(data)

# Add serializers for User, Team, Activity, Leaderboard, Workout here as models are defined
