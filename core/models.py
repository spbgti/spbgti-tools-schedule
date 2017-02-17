from django.db import models

from core.fields import PositionField
from core.fields import RankField
from django.core.urlresolvers import reverse

class Group(models.Model):
    number = models.CharField("Номер группы", max_length=10, unique=True)

    def get_absolute_url(self):
        return reverse('group_by_id', kwargs={'group_id': self.id})

    def to_json(self):
        return dict(group_id=self.id,
                    number=self.number)

    def __str__(self):
        return "%s" % str(self.number)


class Location(models.Model):
    name = models.CharField("Название", max_length=100, unique=True)
    geo_position = models.CharField("Геопозиция", max_length=60, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('location_by_id', kwargs={'location_id': self.id})

    def to_json(self):
        return dict(location_id=self.id,
                    name=self.name,
                    geo_position=self.geo_position)

    def __str__(self):
        return "%s" % str(self.name)


class Room(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField("Название", max_length=50)

    def get_absolute_url(self):
        return reverse('room_by_id', kwargs={'room_id': self.id})

    def to_json(self):
        return dict(room_id=self.id,
                    name=self.name,
                    #location=self.location.to_json()
                    location_id=self.location_id)

    def __str__(self):
        return "{}".format(self.name)#"{} {}".format(self.location.name, self.name)


class Teacher(models.Model):
    name = models.CharField("ФИО", max_length=100)
    rank = RankField('Ученая степень', blank=True, null=True)
    position = PositionField('Должность', blank=True, null=True)
    # кафедра(ы)?

    def get_absolute_url(self):
        return reverse('teacher_by_id', kwargs={'teacher_id': self.id})

    def to_json(self):
        return dict(teacher_id=self.id,
                    name=self.name,
                    rank=self.rank,
                    position=self.position)
                    #rank=self.get_rank_display(),
                    #position=self.get_position_display())

    # TODO make something with null rank
    def __str__(self):
        return "%s %s %s" % (self.get_rank_display(), self.get_position_display(), str(self.name))
