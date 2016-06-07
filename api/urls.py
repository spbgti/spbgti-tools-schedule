from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<group_id>[0-9]+)/$', views.detail, name='detail'),
]

