from rest_framework import serializers
from ..models import list

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = list.List
        fields = ('title', 'board', 'order', 'created_at',)
        read_only_fields = ('created_at', 'update_at')