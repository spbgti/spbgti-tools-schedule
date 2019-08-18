from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api import serializers
from api.models import Schedule, Exercise
from core import models


def get_by_id(queryset, serializer, pk):
    """
    Temporary helper against code duplication.

    Should be removed after API will be rewritten to default id lookup.
    """
    inst = get_object_or_404(queryset, pk=pk)
    serializer = serializer(inst)
    return Response(serializer.data)


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GroupSerializer
    lookup_field = 'number'
    queryset = models.Group.objects.all()

    @action(detail=False, methods=['GET'], url_path='id/(?P<id>[^/.]+)')
    def get_by_id(self, request, id, pk=None):
        return get_by_id(self.get_queryset(), self.get_serializer(), id)


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LocationSerializer
    lookup_field = 'name'
    queryset = models.Location.objects.all()

    @action(detail=False, methods=['GET'], url_path='id/(?P<id>[^/.]+)')
    def get_by_id(self, request, id, pk=None):
        return get_by_id(self.get_queryset(), self.get_serializer(), id)


class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RoomSerializer
    lookup_field = 'name'
    queryset = models.Room.objects.all()

    @action(detail=False, methods=['GET'], url_path='id/(?P<id>[^/.]+)')
    def get_by_id(self, request, id, pk=None):
        return get_by_id(self.get_queryset(), self.get_serializer(), id)

    @action(detail=False, methods=['GET'], url_path='location/(?P<location_id>[^/.]+)')
    def get_by_parent(self, request, location_id, pk=None):
        rooms = self.get_queryset().filter(location_id=location_id)
        serializer = self.get_serializer(rooms, many=True)
        return Response(serializer.data)


class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TeacherSerializer
    lookup_field = 'name'
    queryset = models.Teacher.objects.all()

    @action(detail=False, methods=['GET'], url_path='id/(?P<id>[^/.]+)')
    def get_by_id(self, request, id, pk=None):
        return get_by_id(self.get_queryset(), self.get_serializer(), id)


class ScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ScheduleSerializer
    queryset = Schedule.objects.all()

    @action(detail=False, methods=['GET'], url_path='group/(?P<group_number>[0-9]{1,6}[(]?[A-Za-zА-Яа-я0-9]{0,10}[)]?)/year/(?P<year>[0-9]+)/semester/(?P<semester>[0-9]+)')
    def get_schedule(self, request, group_number, year, semester, pk=None):
        schedule = get_object_or_404(
            self.get_queryset(),
            group__number=group_number,
            year=year,
            semester=semester,
        )
        serializer = self.get_serializer(schedule)
        return Response(serializer.data)


class ExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ExerciseSerializer
    queryset = Exercise.objects.all()

    @action(detail=False, methods=['GET'], url_path='schedule/(?P<schedule_id>[0-9]+)/day/(?P<day>[1-7]+)/pair/(?P<pair>[1-5]+)/parity/(?P<parity>[12]*)')
    def get_exercise(self, request, schedule_id, day, pair, parity, pk=None):
        exercise = get_object_or_404(
            self.get_queryset(),
            schedule_id=schedule_id,
            day=day,
            pair=pair,
            parity=parity or None,
        )
        serializer = self.get_serializer(exercise)
        return Response(serializer.data)
