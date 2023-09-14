from ..models.task import Task
from rest_framework import viewsets, permissions
from ..serializers.task_serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [permissions.AllowAny] 
    serializer_class = TaskSerializer