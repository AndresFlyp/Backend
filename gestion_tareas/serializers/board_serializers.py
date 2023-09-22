from rest_framework import serializers
from ..models.board import Board

class BoardSerializer(serializers.ModelSerializer, ):
    class Meta:
        model = Board
        fields = ['id', 'title']

    def validate_title(self, value):
        
        if Board.objects.filter(title=value).exists():
            raise serializers.ValidationError("There is already a board with this title")
        return value    