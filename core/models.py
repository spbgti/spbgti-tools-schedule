from django.db import models

from core.fields import PositionField
from core.fields import RankField


class Group(models.Model):
    number = models.CharField("Номер группы", max_length=10, unique=True)

    def to_json(self):
        return dict(group_id=self.id,
                    number=self.number)

    def __str__(self):
        return "%s" % str(self.number)


class Location(models.Model):
    name = models.CharField("Название", max_length=100)
    geo_position = models.CharField("Геопозиция", max_length=60, blank=True, null=True)

    def to_json(self):
        return dict(location_id=self.id,
                    name=self.name,
                    geo_position=self.geo_position)

    def __str__(self):
        return "%s" % str(self.name)


class Room(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=50)

    def to_json(self):
        return dict(room_id=self.id,
                    name=self.name,
                    location=self.location.to_json())

    def __str__(self):
        return "%s %s" % (str(self.location.name), str(self.name))


class Teacher(models.Model):
    name = models.CharField("ФИО", max_length=100)
    rank = RankField('Ученая степень', blank=True, null=True)
    position = PositionField('Должность')

    def to_json(self):
        return dict(teacher_id=self.id,
                    name=self.name,
                    rank=self.get_rank_display(),
                    position=self.get_position_display())

    # TODO make something with null rank
    def __str__(self):
        return "%s %s %s" % (self.get_rank_display(), self.get_position_display(), str(self.name))


class Semester(models.Model):
    year = models.CharField("Год", max_length=4, default='2016')
    number = models.CharField("Номер семестра", max_length=1, default='1')

    def to_json(self):
        return dict(semester_id=self.id,
                    year=self.year,
                    number=self.number)

    def __str__(self):
        return "%s.%s" % (str(self.year), str(self.number))
