import json
from datetime import date
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, Http404, HttpRequest

from core.models import *
from api.models import *

'''
url:
api/groups
api/locations
api/rooms
api/teachers
api/schedules
api/exercises

GET:
возвращает список моделей в JSON + 200 или 404 если нет экземпляров
POST:
добавляет модель в бд и возвращает её в JSON + 201 + абсолютную ссылку в заголовке "Location"

Для других методов возвращает 405 и список методов в заголовке Allow
'''
    
@csrf_exempt
def model_get_and_create(request, model):
    if request.method == 'GET':
        models = model.objects.all()
        if not models:
            return HttpResponse('No one %s' % model.__name__, status=404)
        result = dict()
        print([model.__dict__ for model in models])
        result[model.__name__] = [model.to_json() for model in models]
        return JsonResponse(result)
    elif request.method == 'POST':
        if request.content_type == 'application/json':
            try:
                query = json.loads(request.body.decode('utf-8'))
                new_model = model(**query)
                new_model.full_clean()
            except TypeError:
                return HttpResponse("Invalid fields in request", status=400)
            except ValueError:
                return HttpResponse("Invalid JSON", status=400)
            except ValidationError as e:
                return HttpResponse("Invalid fields in request: " + str(e.message_dict), status=400)
            else:
                new_model.save()
                response = JsonResponse(new_model.to_json(), status=201)
                response['Location'] = new_model.get_absolute_url()
                return response
        else:
            return HttpResponse("Permitted content type: application/json", status=400)
    else:
        response = HttpResponse(status=405)
        response['Allow'] = "GET, POST"
        return response

'''
url:
api/groups/{group_number}
api/groups/id/{group_id}

находит группу и передает в обработку в instance_get_put_delete или 404
'''
@csrf_exempt
def group_instance(request, group_id=None, group_number=None):
    group = None
    try:
        if group_id:
            group = Group.objects.get(id=group_id)
        elif group_number:
            group = Group.objects.get(number=group_number)
    except Group.DoesNotExist:
        return HttpResponse("Group not found", status=404)
    return instance_get_put_delete(request, group)
'''
GET:
возвращает экземпляр модели в JSON + 200
PUT:
принимает данные
изменяет экземпляр модели и возвращает её в JSON + 200
400 если есть ошибка в данных
DELETE:
удаляет экземпляр модели и возвращает 200

Для других методов возвращает 405 и список методов в заголовке Allow
'''
@csrf_exempt
def instance_get_put_delete(request, instance):
    if request.method == 'GET':
        return JsonResponse(instance.to_json())
    elif request.method == 'PUT':
        if request.content_type == 'application/json':
            try:
                query = json.loads(request.body.decode('utf-8'))
                model_for_validate = instance.__class__(**query)
                model_for_validate.full_clean()
            except TypeError:
                return HttpResponse("Invalid fields in request", status=400)
            except ValueError:
                print(instance.teacher)
                print(instance.__class__.__dict__)
                return HttpResponse("Invalid JSON", status=400)
            except ValidationError as e:
                return HttpResponse("Invalid fields in request: " + str(e.message_dict), status=400)
            else:
                instance.__dict__.update(**query)
                instance.save()
                return JsonResponse(instance.to_json())
        else:
            return HttpResponse("Permitted content type: application/json", status=400)
    elif request.method == 'DELETE':
        instance.delete()
        return HttpResponse(status=204)
    else:
        response = HttpResponse(status=405)
        response['Allow'] = "GET, PUT, DELETE"
        return response


@csrf_exempt
def location_instance(request, location_id=None, location_name=None):
    location = None
    try:
        if location_id:
            location = Location.objects.get(id=location_id)
        elif location_name:
            location = Location.objects.get(name=location_name)
    except Location.DoesNotExist:
        return HttpResponse("Location not found", status=404)
    return instance_get_put_delete(request, location)


@csrf_exempt
def room_instance(request, room_id=None, location_id=None):
    room = None
    try:
        if room_id:
            room = Room.objects.get(id=room_id)
        elif location_id:
            room = Room.objects.get(location_id=location_id)
    except Room.DoesNotExist:
        return HttpResponse("Room not found", status=404)
    return instance_get_put_delete(request, room)

@csrf_exempt
def teacher_instance(request, teacher_id=None):
    teacher = None
    try:
        if teacher_id:
            teacher = Teacher.objects.get(id=teacher_id)
        else:
            pass
    except Teacher.DoesNotExist:
        return HttpResponse("Teacher not found", status=404)
    return instance_get_put_delete(request, teacher)


@csrf_exempt
def schedule_instance(request, schedule_id=None):
    schedule = None
    try:
        if schedule_id:
            schedule = Schedule.objects.get(id=schedule_id)
        else:
            pass
    except Schedule.DoesNotExist:
        return HttpResponse("Schedule not found", status=404)
    return instance_get_put_delete(request, schedule)

@csrf_exempt
def exercise_get_and_create(request):
    model = Exercise
    if request.method == 'GET':
        models = model.objects.all()
        if not models:
            return HttpResponse('No one %s' % model.__name__, status=404)
        result = dict()
        print([model.__dict__ for model in models])
        result[model.__name__] = [model.to_json() for model in models]
        return JsonResponse(result)
    elif request.method == 'POST':
        if request.content_type == 'application/json':
            try:
                query = json.loads(request.body.decode('utf-8'))
                teachers = query.get('teacher')
                if teachers:
                    del query['teacher']
                    new_model = model(**query)
                    new_model.full_clean()
                    new_model.save()
                    for teacher_id in teachers:
                        if isinstance(teacher_id, int):
                            try:
                                new_model.teacher.add(Teacher.objects.get(id=teacher_id))
                            except Teacher.DoesNotExist:
                                raise TypeError('teacher %d does not exist' % teacher_id)
                        else:
                            raise TypeError('teacher[] not id')
                else:
                    raise TypeError('where teacher[]?')
            except TypeError as e:
                return HttpResponse("Invalid fields in request " + str(e), status=400)
            except ValueError as e:
                return HttpResponse("Invalid JSON " + str(e), status=400)
            except ValidationError as e:
                return HttpResponse("Invalid fields in request: " + str(e.message_dict), status=400)
            else:
                new_model.save()
                response = JsonResponse(new_model.to_json(), status=201)
                response['Location'] = new_model.get_absolute_url()
                return response
        else:
            return HttpResponse("Permitted content type: application/json", status=400)
    else:
        response = HttpResponse(status=405)
        response['Allow'] = "GET, POST"
        return response
    pass

@csrf_exempt
def exercise_instance(request, exercise_id=None):
    exercise = None
    try:
        if exercise_id:
            exercise = Exercise.objects.get(id=exercise_id)
        else:
            pass
    except Exercise.DoesNotExist:
        return HttpResponse("Eexercise not found", status=404)

    if request.method == 'GET':
        return JsonResponse(exercise.to_json())
    elif request.method == 'PUT':
        if request.content_type == 'application/json':
            try:
                query = json.loads(request.body.decode('utf-8'))
                teachers = query.get('teacher')
                if teachers:
                    del query['teacher']
                    model_for_validate = exercise.__class__(**query)
                    model_for_validate.full_clean()
                    exercise.teacher.clear()
                    for teacher_id in teachers:
                        if isinstance(teacher_id, int):
                            try:
                                exercise.teacher.add(Teacher.objects.get(id=teacher_id))
                            except Teacher.DoesNotExist:
                                raise TypeError('teacher %d does not exist' % teacher_id)
                        else:
                            raise TypeError('teacher[] not id')
                else:
                    raise TypeError('where teacher[]?')
            except TypeError:
                return HttpResponse("Invalid fields in request", status=400)
            except ValueError:
                print(exercise.teacher)
                print(exercise.__class__.__dict__)
                return HttpResponse("Invalid JSON", status=400)
            except ValidationError as e:
                return HttpResponse("Invalid fields in request: " + str(e.message_dict), status=400)
            else:
                exercise.__dict__.update(**query)
                exercise.save()
                return JsonResponse(exercise.to_json())
        else:
            return HttpResponse("Permitted content type: application/json", status=400)
    elif request.method == 'DELETE':
        exercise.delete()
        return HttpResponse(status=204)
    else:
        response = HttpResponse(status=405)
        response['Allow'] = "GET, PUT, DELETE"
        return response

# TODO Refactor here to check for any errors. Check if the group exists, check current semester available
# TODO Check schedule exists for this group at this semester
# TODO Think of automatization of error output
def get_schedule_by_group(request, group_number):
    group = Group.objects.get(number=group_number)
    #current_semester = Semester.objects.get(year=date.today().year, number=_get_current_semester())
    #schedule = group.schedule_set.filter(semester=current_semester)

    if schedule:
        result = json.dumps(schedule[0].to_json())
    else:
        result = json.dumps('{"error": "Current semester schedule is not available now"}')

    return HttpResponse(result, content_type='application/json')


def _get_current_semester():
    return '1' if 1 <= date.today().month < 8 else '2'
