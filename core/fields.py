from django.db import models
from django.utils.translation import ugettext as _

DAY_OF_THE_WEEK = {
    '1': _(u'Понедельник'),
    '2': _(u'Вторник'),
    '3': _(u'Среда'),
    '4': _(u'Четверг'),
    '5': _(u'Пятница'),
    '6': _(u'Суббота'),
    '7': _(u'Воскресенье'),
}

PARITY = {
    '1': _(u'Четная'),
    '2': _(u'Нечетная'),
}

TIME_RANGE = {
    '1': _(u'09:30 - 11:00'),
    '2': _(u'11:15 - 12:45'),
    '3': _(u'13:30 - 15:00'),
    '4': _(u'15:15 - 16:45'),
    '5': _(u'17:00 - 18:30'),
}

PAIR = {
    '1': _(u'Первая'),
    '2': _(u'Вторая'),
    '3': _(u'Третья'),
    '4': _(u'Четвертая'),
    '5': _(u'Пятая'),
}

RANK = {
    '1': _(u'к.т.н'),
    '2': _(u'д.т.н.')
}

POSITION = {
    '1': _(u'профессор'),
    '2': _(u'доцент'),
    '3': _(u'старший преподаватель'),
    '4': _(u'ассистент'),
}


class DayOfTheWeekField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = tuple(sorted(DAY_OF_THE_WEEK.items()))
        kwargs['max_length'] = 1
        super(DayOfTheWeekField, self).__init__(*args, **kwargs)


class ParityField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = tuple(sorted(PARITY.items()))
        kwargs['max_length'] = 1
        super(ParityField, self).__init__(*args, **kwargs)


class TimeRangeField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = tuple(sorted(TIME_RANGE.items()))
        kwargs['max_length'] = 1
        super(TimeRangeField, self).__init__(*args, **kwargs)


class PairField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = tuple(sorted(PAIR.items()))
        kwargs['max_length'] = 1
        super(PairField, self).__init__(*args, **kwargs)


class RankField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = tuple(sorted(RANK.items()))
        kwargs['max_length'] = 1
        super(RankField, self).__init__(*args, **kwargs)


class PositionField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = tuple(sorted(POSITION.items()))
        kwargs['max_length'] = 1
        super(PositionField, self).__init__(*args, **kwargs)
