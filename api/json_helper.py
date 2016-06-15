import json
from django.core import serializers


def serialize(obj):
    data = serializers.serialize('json', [obj, ])
    struct = json.loads(data)
    data = json.dumps(struct[0])
    return data


def serialize_list(list_of_objects):
    data = [serialize(obj) for obj in list_of_objects]
    return data
