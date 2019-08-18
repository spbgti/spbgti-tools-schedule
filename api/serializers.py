from rest_framework import serializers
from rest_framework.utils.serializer_helpers import ReturnDict

from core import models
from api import models as api_models


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
    #teachers = TeacherSerializer(many=True, source='teacher')
    teachers = serializers.SerializerMethodField('get_teachers_name')

    def get_teachers_name(self, exercise):
        return [t.name for t in exercise.teacher.all()]

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


