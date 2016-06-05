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

PAIRS = {
    '1': _(u'Первая'),
    '2': _(u'Вторая'),
    '3': _(u'Третья'),
    '4': _(u'Четвертая'),
    '5': _(u'Пятая'),
    '6': _(u'Шестая'),
    '7': _(u'Седьмая'),
}


class DayOfTheWeekField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = tuple(sorted(DAY_OF_THE_WEEK.items()))
        kwargs['max_length'] = 1
        super(DayOfTheWeekField, self).__init__(*args, **kwargs)


class PairField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = tuple(sorted(PAIRS.items()))
        kwargs['max_length'] = 1
        super(PairField, self).__init__(*args, **kwargs)