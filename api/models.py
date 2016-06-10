from django.db import models

from core.models import Group
from core.models import Room
from core.models import Semester
from core.models import Teacher
from fields import DayOfTheWeekField
from fields import PairField


class Schedule(models.Model):
    group = models.ForeignKey(Group)
    semester = models.ForeignKey(Semester)

    # TODO fix this
    def __str__(self):
        return "Группа - " + str(self.group) + \
               ", семестр " + str(self.semester)


class Exercise(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    # TODO should have a list of teachers binded
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    exercise_name = models.CharField("Название занятия", max_length=100)
    pair = PairField("Номер пары", default=1)
    day = DayOfTheWeekField("День недели", default=1)

    def __str__(self):
        return str(self.pair) + " пара" + \
               " в " + str(self.day) + \
               str(self.exercise_name)
