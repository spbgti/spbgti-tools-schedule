from django import forms
from django.views.generic import View
from api.models import Exercise, Schedule
from core.models import Group, Teacher, Room
from django.db.models import Q
from django.shortcuts import render




class MyForm(forms.Form):
    name = forms.CharField(label="Название", required=False, max_length=100, widget=forms.Textarea(attrs={'rows': 3, 'cols':25}))
    types = forms.CharField(label="Типы", required=False)
    room = forms.CharField(label="Локация", required=False)
    teachers = forms.CharField(label="Преподы", required=False, max_length=70)

def get_init(instance):
    initial = {
        'name': '',
        'types': '',
        'room': '',
        'teachers': ''
    }
    if instance is not None:
        initial['name'] = instance.name
        initial['types'] = instance.type
        initial['room'] = instance.room.name
        initial['teachers'] = ', '.join(teacher.name for teacher in instance.teacher.all())
    return initial


class MyView(View):
    MyFormSet = forms.formset_factory(form=MyForm, extra=0)

    def get_teachers(self, names):
        teachers = []
        for name in names:
            teacher, _ = Teacher.objects.get_or_create(name=name)
            teachers.append(teacher)
        return teachers

    def post(self, request, group_number):
        formset = self.MyFormSet(request.POST, request.FILES)
        if formset.is_valid():
            schedule = Schedule.objects.get(semester='2', year='2016', group=Group.objects.get(number=group_number))
            Exercise.objects.filter(schedule=schedule).delete()
            cds = [form.cleaned_data for form in formset]
            for i, cd in enumerate(cds, 1):
                name, room, types, teachers = cd['name'].strip(), cd['room'].strip().replace('\\', '/') or 'на кафедре', \
                                              cd['types'].strip(), cd['teachers'].split(', ')
                if i > 20:
                    day = ((i - 1) // 4) - 4
                else:
                    day = ((i - 1) // 4) + 1
                pair = i % 4 or 4
                if i <= 20:
                    if cd == cds[i+20-1]:
                        parity = None
                    else:
                        parity = 1
                else:
                    if cd == cds[i-20-1]:
                        parity = None
                    else:
                        parity = 2
                if name:
                    exercise, created = Exercise.objects.get_or_create(schedule=schedule, day=day, pair=pair, parity=parity)
                    if created:
                        print(repr(room))
                        exercise.name = name
                        exercise.room = Room.objects.get_or_create(name=room)[0]
                        exercise.type = types
                        exercise.save()
                        exercise.teacher.add(*self.get_teachers(teachers))
                        exercise.save()
        else:
            return render(request, 'schedule.html', {'formset': formset})
        return self.get(request, group_number)

    def get(self, request, group_number):
        schedule = Schedule.objects.get(semester='2', year='2016', group=Group.objects.get(number=group_number))
        raw_exercises = Exercise.objects.filter(Q(schedule=schedule), (Q(parity=None) | Q(parity=1)))
        exercises = []
        for day in range(1, 6):
            for pair in range(1, 5):
                try:
                    exercise = raw_exercises.get(day=day, pair=pair)
                except Exercise.DoesNotExist:
                    exercise = None
                exercises.append(exercise)
        raw_exercises = Exercise.objects.filter(Q(schedule=schedule), (Q(parity=None) | Q(parity=2)))
        for day in range(1, 6):
            for pair in range(1, 5):
                try:
                    exercise = raw_exercises.get(day=day, pair=pair)
                except Exercise.DoesNotExist:
                    exercise = None
                exercises.append(exercise)
        init_data = [get_init(inst) for inst in exercises]
        formset = self.MyFormSet(initial=init_data)
        return render(request, 'schedule.html', {'formset': formset})
