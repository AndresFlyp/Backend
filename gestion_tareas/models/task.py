from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):

    PRIORITY_CHOICES = [
        ("HIGH","HIGH"),
        ("MEDIUM", "MEDIUM"),
        ("LOW","LOW"),
    ]    

    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICES, default="MEDIA")
    user = models.ForeignKey(User, on_delete=models.CASCADE)