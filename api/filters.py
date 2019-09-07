from datetime import date
from typing import Tuple

from django.db.models import Q
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
    group_id = filters.NumberFilter('schedule__group_id')
    date = filters.DateFilter(field_name='date', method='filter_by_date')

    def filter_by_date(self, queryset, name, value: date):
        year, semester, parity, weekday = get_date_parameters(value)
        exercises = queryset.filter(
            Q(parity=None) | Q(parity=parity),
            schedule__year=year,
            schedule__semester=semester,
            day=weekday,
        ).order_by('pair')
        return exercises

    class Meta:
        model = Exercise
        fields = {
            'date': [],
            'group_id': ['exact'],
        }


def get_date_parameters(day_date: date) -> Tuple[str, str, str, int]:
    """
    Extract schedule parameters from date: weekday, semester, year and other.

    TODO: Move it to Exercise Model Manager
    """
    _, week_number, weekday = day_date.isocalendar()
    if week_number % 2:
        parity = '1'
    else:
        parity = '2'

    if day_date.month >= 9 or day_date.month < 2:
        semester = '1'
    else:
        semester = '2'

    year = day_date.year

    return str(year), semester, parity, weekday
