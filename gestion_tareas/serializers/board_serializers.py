from rest_framework import serializers
from ..models import board

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = board.Board
        fields = '__all__'