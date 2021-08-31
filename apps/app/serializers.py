from rest_framework import serializers

from . import models

# Task
class TaskSerializer(serializers.ModelSerializer):
    status = serializers.IntegerField(default=0)

    class Meta:
        model = models.Task
        fields = "__all__"


