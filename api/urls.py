
from django.conf.urls import url
from core import models as core_models
from api import models as api_models
from api import endpoints
from . import views

urlpatterns = [
    url(r'^groups$',
        endpoints.model_get_and_create, {'model': core_models.Group}, name='groups'),
    url(r'^groups/id/(?P<group_id>[0-9]+)$',
        endpoints.group_instance, name='group_by_id'),
    url(r'^groups/(?P<group_number>[0-9]{1,6}[(]?[A-Za-zА-Яа-я]{0,10}[)]?)$',
        endpoints.group_instance, name='group_by_number'),

    url(r'^locations$',
        endpoints.model_get_and_create, {'model': core_models.Location}, name='locations'),
    url(r'^locations/id/(?P<location_id>[0-9]+)$',
        endpoints.location_instance, name='location_by_id'),
    url(r'^locations/(?P<location_name>[а-яА-я\w ]+)$',
        endpoints.location_instance, name='locations_by_name'),
    # locations by geopos?

    url(r'^rooms$',
        endpoints.model_get_and_create, {'model': core_models.Room}, name='rooms'),
    url(r'^rooms/(?P<name>[^\\/]+)$',
        endpoints.room_instance, name='room_by_name'),
    url(r'^rooms/id/(?P<room_id>[0-9]+)$',
        endpoints.room_instance, name='room_by_id'),
    url(r'^rooms/location/(?P<location_id>[0-9]+)$',
        endpoints.room_instance, name='room_by_location_id'),

    url(r'^teachers$',
        endpoints.model_get_and_create, {'model': core_models.Teacher}, name='teachers'),
    url(r'^teachers/(?P<teacher_name>[^0-9]+)$',
        endpoints.teacher_instance, name='teacher_by_name'),
    url(r'^teachers/id/(?P<teacher_id>[0-9]+)$',
        endpoints.teacher_instance, name='teacher_by_id'),

    url(r'^schedules$',
        endpoints.model_get_and_create, {'model': api_models.Schedule}, name='schedules'),
    url(r'^schedules/group/(?P<group_id>[0-9]+)/year/(?P<year>[0-9]+)/semester/(?P<semester>[0-9]+)$',
        endpoints.schedule_instance, name='schedule_by_semester_and_group'),
    url(r'^schedules/id/(?P<schedule_id>[0-9]+)$',
        endpoints.schedule_instance, name='schedule_by_id'),


    url(r'^exercises$',
       endpoints.exercise_get_and_create, name='exercises'),
    url(r'^exercises/schedule/(?P<schedule_id>[0-9]+)/day/(?P<day>[1-7]+)/pair/(?P<pair>[1-5]+)/parity/(?P<parity>[12]*)$',
        endpoints.exercise_instance, name='exercise_by_pair'),
    url(r'^exercises/id/(?P<exercise_id>[0-9]+)$',
        endpoints.exercise_instance, name='exercise_by_id'),
]
'''

   url(r'^schedules/$',
       endpoints.schedules, name='schedules'),
   url(r'^schedules/group/(?P<group_number>[0-9]{1,6}[A-Za-zА-Яа-я]{0,6})$',
       endpoints.schedules_by_group_number, name='schedules_by_group_number'),
   url(r'^schedules/group/(?P<group_number>[0-9]{1,6}[A-Za-zА-Яа-я]{0,6})/(?P<year>20[0-9]{2})/(?P<number>[12])$',
       endpoints.schedule_by_group_number_and_semester, name='schedule_by_group_number_and_semester'),

   url(r'^exercises/$',
       endpoints.exercises, name='exercises'),
   url(r'^exercises/schedule/(?P<schedule_id>[0-9]+)$',
       endpoints.exercises_by_schedule_id, name='exercises_by_schedule_id'),
   url(r'^exercises/room/(?P<room_id>[0-9]+)$',
       endpoints.exercises_by_room_id, name='exercises_by_room_id'),
   url(r'^exercises/teacher/(?P<teacher_id>[0-9]+)$',
       endpoints.exercises_by_teacher_id, name='exercises_by_teacher_id'),
   url(r'^exercises/schedule/(?P<schedule_id>[0-9]+)/parity/(?P<parity_num>[1-2])/day/(?P<day_num>[1-7])/pair/(?P<pair_num>[1-5])$',
       endpoints.exercise_by_place_in_schedule, name='exercise_by_place_in_schedule')
   '''