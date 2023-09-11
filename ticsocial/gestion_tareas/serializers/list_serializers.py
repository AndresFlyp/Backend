from rest_framework import serializers
from ..models import list

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = list.List
        fields = '__all__'