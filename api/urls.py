from django.conf.urls import url

from api import endpoints
from . import views

urlpatterns = [
    url(r'^get_all_groups/$', endpoints.get_all_groups, name='get_all_groups'),
    url(r'^get_schedule_by_group/(?P<group_number>[0-9]+)/$', endpoints.get_schedule_by_group, name='get_schedule_by_group'),
]

