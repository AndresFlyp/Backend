from rest_framework import serializers
from ..models import task


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = task.Task
        fields = '__all__'