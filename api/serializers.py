from rest_framework import serializers
from rest_framework.utils.serializer_helpers import ReturnDict

from core import models


class GroupSerializer(serializers.ModelSerializer):
    group_id = serializers.IntegerField(source='id')

    class Meta:
        model = models.Group
        fields = [
            'group_id',
            'number',
        ]


class LocationSerializer(serializers.ModelSerializer):
    location_id = serializers.IntegerField(source='id')

    class Meta:
        model = models.Location
        fields = [
            'location_id',
            'name',
            'geo_position',
        ]


class RoomSerializer(serializers.ModelSerializer):
    room_id = serializers.IntegerField(source='id')

    class Meta:
        model = models.Room
        fields = [
            'room_id',
            'name',
            'location_id',
        ]