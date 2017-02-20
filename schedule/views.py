from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from api.models import Schedule


def index(request):
    groups = Schedule.objects.order_by('-group')
    context = {'groups': groups}
    return render(request, 'schedule/index.html', context)


def detail(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    return render(request, 'schedule/detail.html', {'group': schedule.group})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
