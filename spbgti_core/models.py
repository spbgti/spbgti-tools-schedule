from django.db import models

from spbgti_core.fields import PositionField, RANK, POSITION
from spbgti_core.fields import RankField


class Group(models.Model):
    number = models.CharField("Номер группы", max_length=10)

    def __str__(self):
        return "" + str(self.number)


class Location(models.Model):
    name = models.CharField("Название", max_length=100)
    geo_position = models.CharField("Геопозиция", max_length=60)

    def __str__(self):
        return "" + str(self.name)


class Room(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=50)

    def __str__(self):
        return "" + str(self.location.name) + " " + str(self.name)


class Teacher(models.Model):
    name = models.CharField("ФИО", max_length=100)
    rank = RankField('Ученая степень', blank=True, null=True)
    position = PositionField('Должность')

    # TODO some time we should fix it / move str to fields
    def __str__(self):
        return "" + str(RANK[str(self.rank)]) \
               + " " + str(POSITION[str(self.position)]) \
               + " " + str(self.name)


class Semester(models.Model):
    number = models.CharField("Семестр", max_length=20)

    def __str__(self):
        return "" + str(self.number)
