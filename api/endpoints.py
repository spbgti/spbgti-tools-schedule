from django.http import JsonResponse

from api.json_helper import serialize, serialize_list
from core.models import Group


def get_all_groups(request):
    return JsonResponse(serialize_list(Group.objects.all()), safe=False)


def get_schedule_by_group(request, group_number):
    return JsonResponse(serialize(Group.objects.get(number=group_number)), safe=False)
