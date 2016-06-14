from django.db import models

from core.fields import PositionField
from core.fields import RankField


class Group(models.Model):
    number = models.CharField("Номер группы", max_length=10)

    def __str__(self):
        return "%s" % str(self.number)


class Location(models.Model):
    name = models.CharField("Название", max_length=100)
    geo_position = models.CharField("Геопозиция", max_length=60, blank=True, null=True)

    def __str__(self):
        return "%s" % str(self.name)


class Room(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=50)

    def __str__(self):
        return "%s %s" % (str(self.location.name), str(self.name))


class Teacher(models.Model):
    name = models.CharField("ФИО", max_length=100)
    rank = RankField('Ученая степень', blank=True, null=True)
    position = PositionField('Должность')

    # TODO make something with null rank
    def __str__(self):
        return "%s %s %s" % (self.get_rank_display(), self.get_position_display(), str(self.name))


class Semester(models.Model):
    number = models.CharField("Семестр", max_length=20)

    def __str__(self):
        return "%s" % str(self.number)
