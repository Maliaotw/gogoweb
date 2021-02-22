from django.shortcuts import render
from . import models
from . import serializers

from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView, Response
from rest_framework import status

# Create your views here.
class TaskModelViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    pagination_class = LimitOffsetPagination

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)

