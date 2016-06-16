import json
from datetime import date

from django.http import HttpResponse

from core.models import Group, Semester


def get_all_groups(request):
    result = json.dumps([group.to_json() for group in Group.objects.all()])
    return HttpResponse(result, content_type='application/json')


# TODO Refactor here to check for any errors. Check if the group exists, check current semester available
# TODO Check schedule exists for this group at this semester
# TODO Think of automatization of error output
def get_schedule_by_group(request, group_number):
    group = Group.objects.get(number=group_number)
    current_semester = Semester.objects.get(year=date.today().year, number=_get_current_semester())
    schedule = group.schedule_set.filter(semester=current_semester)

    if schedule:
        result = json.dumps(schedule[0].to_json())
    else:
        result = json.dumps('{"error": "Current semester schedule is not available now"}')

    return HttpResponse(result, content_type='application/json')


def _get_current_semester():
    return '1' if 1 <= date.today().month < 8 else '2'
