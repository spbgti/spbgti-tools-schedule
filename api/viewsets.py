from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api import serializers
from core import models


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GroupSerializer
    lookup_field = 'number'
    queryset = models.Group.objects.all()

    @action(detail=False, methods=['GET'], url_path='id/(?P<id>[^/.]+)')
    def get_by_id(self, request, id, pk=None):
        group = get_object_or_404(self.get_queryset(), pk=id)
        serializer = self.get_serializer(group)
        return Response(serializer.data)


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LocationSerializer
    lookup_field = 'name'
    queryset = models.Location.objects.all()

    @action(detail=False, methods=['GET'], url_path='id/(?P<id>[^/.]+)')
    def get_by_id(self, request, id, pk=None):
        location = get_object_or_404(self.get_queryset(), pk=id)
        serializer = self.get_serializer(location)
        return Response(serializer.data)


class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RoomSerializer
    lookup_field = 'name'
    queryset = models.Room.objects.all()

    @action(detail=False, methods=['GET'], url_path='id/(?P<id>[^/.]+)')
    def get_by_id(self, request, id, pk=None):
        location = get_object_or_404(self.get_queryset(), pk=id)
        serializer = self.get_serializer(location)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'], url_path='location/(?P<location_id>[^/.]+)')
    def get_by_parent(self, request, location_id, pk=None):
        rooms = self.get_queryset().filter(location_id=location_id)
        serializer = self.get_serializer(rooms, many=True)
        return Response(serializer.data)

