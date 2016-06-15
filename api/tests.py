from unittest import TestCase

from api import endpoints
from api.test_helpers import fill_database, are_json_objects_equal
from core.models import Room, Location


class RoomTestCase(TestCase):
    location_name = "Кафедра САПРиУ"
    room_name = "ауд. 6"

    def setUp(self):
        Room.objects.create(name=self.room_name,
                            location=Location.objects.create(name=self.location_name, geo_position="None"))

    def test_room_str_is_equal_to_location_str(self):
        room = Room.objects.get(pk=1)
        self.assertEqual(str(room), self.location_name + " " + self.room_name)


class ScheduleEndpointsTestCase(TestCase):
    get_all_groups_expected_response = '[{"number": "459", "group_id": 1}]'
    get_schedule_by_group_response = '{"number": "459", "group_id": 1}'

    @fill_database
    def test_get_all_groups(self):
        """
        Test the get_all_groups api call.
        Based on previous temp base filling it should return 'get_all_groups_expected_response' response
        """
        response = endpoints.get_all_groups(None)
        self.assertTrue(are_json_objects_equal(
            self.get_all_groups_expected_response,
            response.content.decode('ascii')
        ))

    @fill_database
    def test_get_schedule_by_group(self):
        """
        Test the get_schedule_by_group api call.
        Based on previous temp base filling it should return 'get_schedule_by_group_response' response
        """
        response = endpoints.get_schedule_by_group(None, '459')
        self.assertTrue(are_json_objects_equal(
            self.get_schedule_by_group_response,
            response.content.decode('ascii')
        ))
