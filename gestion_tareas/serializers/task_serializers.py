from rest_framework import serializers
from ..models import task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task.Task
        fields = ('title', 'description', 'important',)
        read_only_fields = ('created','datecompleted', 'user',)
        