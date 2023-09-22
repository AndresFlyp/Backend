from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from ..models.task import Task
from ..serializers.task_serializers import TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['priority']
    ordering_fields = ['created', 'priority']
    search_fields = ['title', 'description']

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
