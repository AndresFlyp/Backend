from django.db import models
from .board import Board

class List(models.Model):
    title = models.CharField(max_length=200)
    board = models.ForeignKey(Board, related_name='lists', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)