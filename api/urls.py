
from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from core import models as core_models
from api import models as api_models, viewsets
from api import endpoints
from . import views
router = SimpleRouter(trailing_slash=False)
router.register('groups', viewsets.GroupViewSet)
router.register('locations', viewsets.LocationViewSet)
router.register('rooms', viewsets.RoomViewSet)
router.register('teachers', viewsets.TeacherViewSet)
router.register('schedules', viewsets.ScheduleViewSet)
router.register('exercises', viewsets.ExerciseViewSet)
urlpatterns = router.urls