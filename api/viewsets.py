from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api import serializers
from core import models


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GroupSerializer
    keyword = 'groups'
    lookup_field = 'number'
    queryset = models.Group.objects.all()

    @action(detail=False, methods=['GET'], url_path='id/(?P<id>[^/.]+)')
    def get_by_id(self, request, id, pk=None):
        group = get_object_or_404(self.get_queryset(), pk=id)
        serializer = self.get_serializer(group)
        return Response(serializer.data)