
from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from core import models as core_models
from api import models as api_models, viewsets
from api import endpoints
from . import views
router = SimpleRouter(trailing_slash=False)
router.register('groups', viewsets.GroupViewSet)
urlpatterns = router.urls

urlpatterns += [
    url(r'^locations$',
        endpoints.LocationView.as_view(), name='locations'),
    url(r'^locations/id/(?P<location_id>[0-9]+)$',
        endpoints.LocationView.as_view(), name='location_by_id'),
    url(r'^locations/(?P<location_name>[а-яА-я\w ]+)$',
        endpoints.LocationView.as_view(), name='locations_by_name'),
    # locations by geopos?

    url(r'^rooms$',
        endpoints.RoomView.as_view(), name='rooms'),
    url(r'^rooms/(?P<name>[^\\/]+)$',
        endpoints.RoomView.as_view(), name='room_by_name'),
    url(r'^rooms/id/(?P<room_id>[0-9]+)$',
        endpoints.RoomView.as_view(), name='room_by_id'),
    url(r'^rooms/location/(?P<location_id>[0-9]+)$',
        endpoints.RoomView.as_view(), name='room_by_location_id'),

    url(r'^teachers$',
        endpoints.TeacherView.as_view(), name='teachers'),
    url(r'^teachers/(?P<teacher_name>[^0-9]+)$',
        endpoints.TeacherView.as_view(), name='teacher_by_name'),
    url(r'^teachers/id/(?P<teacher_id>[0-9]+)$',
        endpoints.TeacherView.as_view(), name='teacher_by_id'),

    url(r'^schedules$',
        endpoints.ScheduleView.as_view(), name='schedules'),
    url(r'^schedules/group/(?P<group_number>[0-9]{1,6}[(]?[A-Za-zА-Яа-я0-9]{0,10}[)]?)/year/(?P<year>[0-9]+)/semester/(?P<semester>[0-9]+)$',
        endpoints.ScheduleView.as_view(), name='schedule_by_semester_and_group'),
    url(r'^schedules/id/(?P<schedule_id>[0-9]+)$',
        endpoints.ScheduleView.as_view(), name='schedule_by_id'),


    url(r'^exercises$',
       endpoints.ExerciseView.as_view(), name='exercises'),
    url(r'^exercises/schedule/(?P<schedule_id>[0-9]+)/day/(?P<day>[1-7]+)/pair/(?P<pair>[1-5]+)/parity/(?P<parity>[12]*)$',
        endpoints.ExerciseView.as_view(), name='exercise_by_pair'),
    url(r'^exercises/id/(?P<exercise_id>[0-9]+)$',
        endpoints.ExerciseView.as_view(), name='exercise_by_id'),
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