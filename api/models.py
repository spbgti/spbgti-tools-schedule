from django.db import models

from spbgti_core.fields import DayOfTheWeekField
from spbgti_core.fields import PairField
from spbgti_core.models import Group
from spbgti_core.models import Room
from spbgti_core.models import Semester
from spbgti_core.models import Teacher


class Schedule(models.Model):
    group = models.ForeignKey(Group)
    semester = models.ForeignKey(Semester)

    def __str__(self):
        return "Группа - %s, семестр %s" % \
               (str(self.group), str(self.semester))


class Exercise(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    # TODO should have a list of teachers binded
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    exercise_name = models.CharField("Название занятия", max_length=100)
    pair = PairField("Номер пары", default=1)
    day = DayOfTheWeekField("День недели", default=1)

    def __str__(self):
        return "%s пара в %s, %s" % \
               (self.get_pair_display(), self.get_day_display(), str(self.exercise_name))
