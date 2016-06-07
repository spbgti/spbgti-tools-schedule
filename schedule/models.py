from django.db import models
from django.utils import timezone

from fields import DayOfTheWeekField
from fields import PairField


class Schedule(models.Model):
    group = models.IntegerField("Номер группы")
    year = models.DateField("Год", default=timezone.now)
    semester = models.IntegerField("Номер семестра")

    # TODO fix the model - year shouldn't be date
    def __str__(self):
        return "Группа - " + str(self.group) + \
               ", год " + str(self.year.year) + \
               ", семестр " + str(self.semester)


class ClassRecord(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    pair = PairField("Номер пары", default=1)
    day = DayOfTheWeekField("День недели", default=1)
    class_name = models.CharField("Название занятия", max_length=100, blank=True, null=True)
    place = models.CharField("Место проведения", max_length=100, blank=True, null=True)
    teacher = models.CharField("Преподаватель", max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.pair) + " пара" + \
               "в " + str(self.day) + \
               str(self.class_name)
