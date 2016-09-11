from datetime import date
from unittest import TestCase

from api import endpoints
from api.models import Schedule, Exercise
from api.test_helpers import fill_database, is_object_equal_to_json
from core.models import Room, Location, Teacher, Group


def _fill_base_for_tests():
    global location, room, teacher, group, semester, schedule, exercise

    location = Location.objects.create(name='Кафедра САПРиУ')
    room = Room.objects.create(name='ауд. 6', location=location)

    teacher = Teacher.objects.create(name='Макарук Роман Валерьевич', rank='1', position='3')

    group = Group.objects.create(number='459')

    year = date.today().year
    number = '1' if 1 <= date.today().month < 8 else '2'

    schedule = Schedule.objects.create(group=group, year=str(year), semester=number)

    exercise = Exercise.objects.create(schedule=schedule,
                                       room=room,
                                       name='Факультатив UNIX',
                                       pair='1',  # Первая
                                       day='1',  # Понедельник
                                       parity='1'  # Четная
                                       )
    exercise.teacher.add(teacher)
    exercise.save()

'''
class ScheduleEndpointsTestCase(TestCase):
    @fill_database(_fill_base_for_tests)
    def test_get_all_groups(self):
        """
        Test the get_all_groups api call.
        Based on previous temp base filling it should return 'get_all_groups_expected_response' response
        """
        global group
        response = endpoints.model_get_and_create(None)
        self.assertTrue(
            is_object_equal_to_json([group.to_json()], response.content.decode('ascii'))
        )

    @fill_database(_fill_base_for_tests)
    def test_get_schedule_by_group(self):
        """
        Test the get_schedule_by_group api call.
        Based on previous temp base filling it should return 'get_schedule_by_group_response' response
        """
        global schedule
        response = endpoints.get_schedule_by_group(None, '459')
        self.assertTrue(
            is_object_equal_to_json(schedule.to_json(), response.content.decode('ascii'))
        )
'''