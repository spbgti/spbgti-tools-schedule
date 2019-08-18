from rest_framework.routers import SimpleRouter

from api import viewsets

router = SimpleRouter(trailing_slash=False)
router.register('groups', viewsets.GroupViewSet)
router.register('locations', viewsets.LocationViewSet)
router.register('rooms', viewsets.RoomViewSet)
router.register('teachers', viewsets.TeacherViewSet)
router.register('schedules', viewsets.ScheduleViewSet)
router.register('exercises', viewsets.ExerciseViewSet)
urlpatterns = router.urls
