import json

from django.http import JsonResponse, HttpResponse

from core.models import Group


def get_all_groups(request):
    return HttpResponse(json.dumps([obj.to_json() for obj in Group.objects.all()]), content_type='application/json')


def get_schedule_by_group(request, group_number):
    return HttpResponse(json.dumps(Group.objects.get(number=group_number).to_json()), content_type='application/json')
