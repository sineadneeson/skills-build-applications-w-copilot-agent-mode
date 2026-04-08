from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from activities.models import Activity
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        Activity.objects.all().delete()
        # Teams and Leaderboard will be handled as collections directly
        db = connection.cursor().db_conn.client['octofit_db']
        db.teams.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create users (superheroes)
        marvel_users = [
            {'username': 'ironman', 'email': 'ironman@marvel.com'},
            {'username': 'captainamerica', 'email': 'cap@marvel.com'},
            {'username': 'spiderman', 'email': 'spiderman@marvel.com'},
        ]
        dc_users = [
            {'username': 'batman', 'email': 'batman@dc.com'},
            {'username': 'superman', 'email': 'superman@dc.com'},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com'},
        ]
        marvel_team = {'name': 'Team Marvel', 'members': [u['email'] for u in marvel_users]}
        dc_team = {'name': 'Team DC', 'members': [u['email'] for u in dc_users]}

        for u in marvel_users + dc_users:
            User.objects.create_user(username=u['username'], email=u['email'], password='password')

        # Insert teams
        db.teams.insert_many([marvel_team, dc_team])

        # Create activities
        activities = [
            Activity(user=User.objects.get(email='ironman@marvel.com'), name='Run', duration=30),
            Activity(user=User.objects.get(email='batman@dc.com'), name='Swim', duration=45),
        ]
        Activity.objects.bulk_create(activities)

        # Insert leaderboard
        db.leaderboard.insert_many([
            {'team': 'Team Marvel', 'points': 100},
            {'team': 'Team DC', 'points': 90},
        ])

        # Insert workouts
        db.workouts.insert_many([
            {'name': 'Pushups', 'difficulty': 'Easy'},
            {'name': 'Sprints', 'difficulty': 'Hard'},
        ])

        # Ensure unique index on email for users
        db['users'].create_index('email', unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
