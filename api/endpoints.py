import json
from datetime import date
from django.core.exceptions import ValidationError
from django.db.models import Model
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, Http404, HttpRequest
from django.views.generic import View
from core.models import *
from api.models import *

def _get_current_semester():
    return '1' if 1 <= date.today().month < 8 else '2'


class BaseView(View):
    model = Model

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        if not kwargs and request.method in ['GET', 'POST']:
            return getattr(self, request.method.lower())(request)
        elif kwargs and request.method in ['GET', 'PUT', 'DELETE']:
            inst = self.instance_by_data(**kwargs)
            if inst is not None:
                return getattr(self, request.method.lower()+'_instance')(request, inst)
            else:
                return HttpResponse("{} not found".format(self.model.__name__), status=404)
        else:
            #TODO: работает неправильно - возвращает не те методы + должно возвращать разные методы для разных путей
            return self.http_method_not_allowed(request, *args, **kwargs)

    def instance_by_data(self, **kwargs):
        """Возвращает инстанс модели или None, если такой нет"""
        raise NotImplementedError

    def get_instance(self, request, inst):
        """GET запрос для инстанса модели"""
        return JsonResponse(inst.to_json())

    def put_instance(self, request, inst):
        """PUT запрос для инстанса модели"""
        if request.content_type == 'application/json':
            try:
                query = json.loads(request.body.decode('utf-8'))
                print(query)
                inst.__dict__.update(**query)
                inst.full_clean()
            except TypeError:
                return HttpResponse("Invalid fields in request", status=400)
            except ValueError:
                return HttpResponse("Invalid JSON", status=400)
            except ValidationError as e:
                return HttpResponse("Invalid fields in request: " + str(e.message_dict), status=400)
            else:
                try:
                    inst.save(update_fields=query.keys())
                except ValueError as e:
                    return HttpResponse("Invalid fields in request: " + str(e), status=400)
                response = JsonResponse(inst.to_json(), status=201)
                response['Location'] = inst.get_absolute_url()
                return response
        else:
            return HttpResponse("Permitted content type: application/json", status=400)

    def delete_instance(self, request, inst):
        """DELETE запрос для инстанса модели"""
        inst.delete()
        return HttpResponse(status=204)

    def get(self, request):
        models = self.model.objects.all()
        if not models:
            models = []
        return JsonResponse([model.to_json() for model in models], safe=False)

    def post(self, request):
        if request.content_type == 'application/json':
            try:
                query = json.loads(request.body.decode('utf-8'))
                print(query)
                new_model = self.model(**query)
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


class GroupView(BaseView):
    model = Group

    def instance_by_data(self, group_id=None, group_number=None):
        try:
            if group_id is not None:
                return self.model.objects.get(id=group_id)
            elif group_number is not None:
                return self.model.objects.get(number=group_number)
        except self.model.DoesNotExist:
            return None


class LocationView(BaseView):
    model = Location

    def instance_by_data(self, location_id=None, location_name=None):
        try:
            if location_id is not None:
                return self.model.objects.get(id=location_id)
            elif location_name is not None:
                return self.model.objects.get(name=location_name)
        except self.model.DoesNotExist:
            return None


class RoomView(BaseView):
    model = Room

    def instance_by_data(self, room_id=None, name=None):
        try:
            if room_id is not None:
                return self.model.objects.get(id=room_id)
            # TODO: должен выдавать список (на GET): научиться обрабатывать списки в get_instance
            #elif location_id is not None:
            #    return self.model.objects.get(location_id=location_id)
            elif name is not None:
                return self.model.objects.get(name=name)
        except self.model.DoesNotExist:
            return None


class TeacherView(BaseView):
    model = Teacher

    def instance_by_data(self, teacher_id=None, teacher_name=None):
        try:
            if teacher_id is not None:
                return self.model.objects.get(id=teacher_id)
            elif teacher_name is not None:
                return self.model.objects.get(name=teacher_name)
        except self.model.DoesNotExist:
            return None


class ScheduleView(BaseView):
    model = Schedule

    def instance_by_data(self, schedule_id=None, semester=None, year=None, group_number=None):
        try:
            if schedule_id is not None:
                return self.model.objects.get(id=schedule_id)
            elif semester and year and group_number:
                return self.model.objects.get(group=Group.objects.get(number=group_number),
                                              semester=semester, year=year)
        except self.model.DoesNotExist:
            return None
        except Group.DoesNotExist:
            return None


class ExerciseView(BaseView):
    model = Exercise

    def instance_by_data(self,  exercise_id=None, schedule_id=None, day=None, pair=None, parity=None):
        try:
            if exercise_id is not None:
                return self.model.objects.get(id=exercise_id)
            elif day and pair and schedule_id and parity:
                return Exercise.objects.get(schedule_id=schedule_id, day=day, pair=pair, parity=parity)
        except self.model.DoesNotExist:
            return None

    def put_instance(self, request, inst):
        if request.content_type == 'application/json':
            try:
                query = json.loads(request.body.decode('utf-8'))
                teachers = self.get_teachers(query.get('teachers'))
                del query['teachers']
                inst.__dict__.update(**query)
                inst.teacher.add(*teachers)
            except TypeError as e:
                return HttpResponse("Invalid fields in request " + str(e), status=400)
            except ValueError as e:
                return HttpResponse("Invalid JSON " + str(e), status=400)
            except ValidationError as e:
                return HttpResponse("Invalid fields in request: " + str(e.message_dict), status=400)
            else:
                try:
                    inst.save(update_fields=query.keys())
                except ValueError as e:
                    return HttpResponse("Invalid fields in request: " + str(e), status=400)
                response = JsonResponse(inst.to_json(), status=201)
                response['Location'] = inst.get_absolute_url()
                return response
        else:
            return HttpResponse("Permitted content type: application/json", status=400)

    def post(self, request):
        if request.content_type == 'application/json':
            try:
                query = json.loads(request.body.decode('utf-8'))
                teachers = self.get_teachers(query.get('teachers'))
                del query['teachers']
                new_model = self.model(**query)
                new_model.full_clean()
                new_model.save()
                new_model.teacher.add(*teachers)
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

    def get_teachers(self, ids):
        if ids is None:
            raise TypeError('teachers[] not id')
        teachers = []
        for teacher_id in ids:
            try:
                teachers.append(Teacher.objects.get(id=teacher_id))
            except Teacher.DoesNotExist:
                raise TypeError('teacher {} does not exist'.format(teacher_id))
        return teachers
