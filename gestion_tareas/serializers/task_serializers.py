from rest_framework import serializers
from ..models.task import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'priority',)
        read_only_fields = ('created','datecompleted', 'user',)
        