import json

from core.models import Group

filled = False


def fill_database(test):
    def test_wrapper(self):
        global filled
        if not filled:
            Group.objects.create(number='459')
            filled = True
        test(self)

    return test_wrapper


def are_json_objects_equal(jobj1, jobj2):
    obj1 = json.loads(jobj1)
    obj2 = json.loads(jobj2)

    return obj1 == obj2
