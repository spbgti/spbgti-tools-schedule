from rest_framework import viewsets

from api import serializers, filters
from api.models import Schedule, Exercise
from core import models


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GroupSerializer
    queryset = models.Group.objects.all()
    filterset_class = filters.GroupFilter


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LocationSerializer
    queryset = models.Location.objects.all()
    filterset_class = filters.LocationFilter


class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RoomSerializer
    queryset = models.Room.objects.all()
    filterset_class = filters.RoomFilter


class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TeacherSerializer
    queryset = models.Teacher.objects.all()
    filterset_class = filters.TeacherFilter


class ScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ScheduleSerializer
    queryset = Schedule.objects.all()
    filterset_class = filters.ScheduleFilter


class ExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ExerciseSerializer
    queryset = Exercise.objects.all()
    filterset_class = filters.ExerciseFilter