from ..models.board import Board
from rest_framework import viewsets, permissions
from ..serializers.board_serializers import BoardSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    permission_classes = [permissions.AllowAny] 
    serializer_class = BoardSerializer
