from django.db import models
from core.models import Group
from core.models import Room
from core.models import Teacher

from core.fields import DayOfTheWeekField
from core.fields import PairField
from core.fields import ParityField

from django.core.urlresolvers import reverse

class Schedule(models.Model):
    group = models.ForeignKey(Group)
    year = models.CharField("Год", max_length=4, default='2016')
    semester = models.CharField("Номер семестра", max_length=1, default='1')

    def get_absolute_url(self):
        return reverse('schedule_by_id', kwargs={'schedule_id': self.id})

    def to_json(self):
        return dict(schedule_id=self.id,
                    group_id=self.group_id,
                    year=self.year,
                    semester=self.semester,
                    exercises=[exercise.to_json() for exercise in self.exercise_set.all()])

    def __str__(self):
        return "Группа - %s, %s год %s семестр" % \
               (str(self.group), str(self.year), str(self.semester))


class Exercise(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    teacher = models.ManyToManyField(Teacher, blank=True)

    name = models.CharField("Название занятия", max_length=120, blank=True)
    type = models.CharField("Тип пары", max_length=100, null=True, blank=True)
    pair = PairField("Номер пары", default=1)
    day = DayOfTheWeekField("День недели", default=1)
    parity = ParityField("Четность", default=1, null=True, blank=True)


    def get_absolute_url(self):
        return reverse('exercise_by_id', kwargs={'exercise_id': self.id})

    def to_json(self):
        return dict(exercise_id=self.id,
                    schedule_id=self.schedule.id,
                    #room=self.room.to_json(),
                    room_id=self.room.id,
                    teachers=[teacher.name for teacher in self.teacher.all()],
                    name=self.name,
                    type=self.type,
                    #pair=self.get_pair_display(),
                    #day=self.get_day_display(),
                    #parity=self.get_parity_display())
                    pair=self.pair,
                    day=self.day,
                    parity=self.parity)

    def __str__(self):
        return "%s пара в %s, %s" % \
               (self.get_pair_display(), self.get_day_display(), str(self.name))
