from django.db import models
from .list import List
from .user import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_data = models.DateField(blank=True, null=True)
    list = models.ForeignKey(List, related_name='tasks', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey(User, related_name='tasks_assigned', on_delete=models.SET_NULL, blank=True, null=True)