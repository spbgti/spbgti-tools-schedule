from rest_framework import serializers

from core import models
from api import models as api_models


class SlugRelatedFieldWithCreation(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        instance = self.get_queryset().filter(**{self.slug_field: data}).first()
        if instance is None:
            instance = self.get_queryset().create(**{self.slug_field: data})
        return instance


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


class TeacherSerializer(serializers.ModelSerializer):
    teacher_id = serializers.IntegerField(source='id')

    class Meta:
        model = models.Teacher
        fields = [
            'teacher_id',
            'name',
            'rank',
            'position',
        ]


class ExerciseSerializer(serializers.ModelSerializer):
    exercise_id = serializers.IntegerField(source='id')
    teachers = SlugRelatedFieldWithCreation(
        slug_field='name',
        many=True,
        queryset=models.Teacher.objects.all(),
    )

    class Meta:
        model = api_models.Exercise
        fields = [
            'exercise_id',
            'schedule_id',
            'room_id',
            'teachers',
            'name',
            'type',
            'pair',
            'day',
            'parity',
        ]


class ScheduleSerializer(serializers.ModelSerializer):
    schedule_id = serializers.IntegerField(source='id')
    exercises = ExerciseSerializer(many=True, source='exercise_set')

    class Meta:
        model = api_models.Schedule
        fields = [
            'schedule_id',
            'group_id',
            'year',
            'semester',
            'exercises',
        ]


