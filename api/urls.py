from django.conf.urls import url

from api import endpoints
from . import views

urlpatterns = [
    url(r'^groups/$', endpoints.groups, name='groups'),
    url(r'^groups/(?P<group_number>[0-9]{1,6}[A-Za-zА-Яа-я]{0,6})$', endpoints.groups_by_number, name='group_by_number'),

    url(r'^locations/$', endpoints.locations, name='locations'),
    url(r'^locations/(?P<name>.+)$', endpoints.locations_by_name, name='locations_by_name'),
    # locations by geopos?

    url(r'^rooms/$', endpoints.rooms, name='rooms'),
    url(r'^rooms/(?P<name>.+)$', endpoints.rooms_by_name, name='rooms_by_name'),
    url(r'^rooms/location/(?P<locations>.+)$', endpoints.rooms_in_location, name="rooms_in_location"),

    url(r'^teachers/$', endpoints.teachers, name='teachers'),
    url(r'^teachers/(?P<name>.+)$', endpoints.teachers_by_name, name='teachers_by_name'),

    url(r'^semesters/$', endpoints.semesters, name='semesters'),
    url(r'^semesters/(?P<year>20[0-9]{2})/(?P<number>[12])$', endpoints.semester_by_year_and_number, name='semester_by_year_and_number'),
    url(r'^semesters/year/(?P<year>20[0-9]{2})/number/(?P<number>[12])$'

    url(r'^schedules/$', endpoints.schedules, name='schedules'),
    url(r'^schedules/group/(?P<group_number>[0-9]{1,6}[A-Za-zА-Яа-я]{0,6})$', endpoints.schedules_by_group_number, name='schedules_by_group_number'),
    url(r'^schedules/group/(?P<group_number>[0-9]{1,6}[A-Za-zА-Яа-я]{0,6})/(?P<year>20[0-9]{2})/(?P<number>[12])$', endpoints.schedule_by_group_number_and_semester, name='schedule_by_group_number_and_semester'),
    url(r'^exercises/$', endpoints.exercises, name='exercises'),
    url(r'^exercises/$', endpoints.exercises, name='exercises'),

]
