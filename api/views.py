from django.shortcuts import render

from api.models import Schedule


def detail(request, group_id):
    groups = Schedule.objects.order_by('-group')
    context = {'groups': groups}
    return render(request, 'schedule/index.html', context)