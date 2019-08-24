from django_filters import rest_framework as filters

from api.models import Schedule, Exercise
from core import models


class GroupFilter(filters.FilterSet):
    class Meta:
        model = models.Group
        fields = {
            'number': ['exact'],
        }


class LocationFilter(filters.FilterSet):
    class Meta:
        model = models.Location
        fields = {
            'name': ['exact'],
        }


class RoomFilter(filters.FilterSet):
    class Meta:
        model = models.Room
        fields = {
            'name': ['exact'],
            'location': ['exact'],
        }


class TeacherFilter(filters.FilterSet):
    class Meta:
        model = models.Teacher
        fields = {
            'name': ['exact'],
        }


class ScheduleFilter(filters.FilterSet):
    group_number = filters.CharFilter('group__number', lookup_expr='iexact')

    class Meta:
        model = Schedule
        fields = {
            'group_number': [],
            'group': ['exact'],
            'year': ['exact'],
            'semester': ['exact'],
        }


class ExerciseFilter(filters.FilterSet):
    # TODO: make it better, now it isn't sensitive for both-parity exercises
    # for example: I want to get exercise for "first week" and it's parity "1"
    # But if exercise has no parity (both week exercise) i get nothing. In this case
    # parity=1 should means parity=None or parity=1
    class Meta:
        model = Exercise
        fields = {
            'schedule': ['exact'],
            'day': ['exact'],
            'pair': ['exact'],
            'parity': ['exact'],
        }
