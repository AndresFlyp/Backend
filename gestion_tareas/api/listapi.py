from ..models.list import List
from rest_framework import viewsets, permissions
from ..serializers.list_serializers import ListSerializer


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    permission_classes = [permissions.AllowAny] 
    serializer_class = ListSerializer