from rest_framework import serializers
from rest_framework.utils.serializer_helpers import ReturnDict

from core import models


class ListAsObjectSerializer(serializers.ListSerializer):
    """
    Convert classic drf list view to object view using `keyword` attr from serializer.

    Classic response: `[{"key": value, ...}, ...]`
    List as object: `{"keyword": [{"key": value, ...}, ...]}`
    """

    @property
    def data(self):
        data = super().data
        ret = {self.child.keyword: data}
        print(ret)
        return ReturnDict(ret, serializer=data.serializer)


class GroupSerializer(serializers.ModelSerializer):
    group_id = serializers.IntegerField(source='id')
    keyword = 'groups'

    class Meta:
        list_serializer_class = ListAsObjectSerializer
        model = models.Group
        fields = [
            'group_id',
            'number',
        ]
