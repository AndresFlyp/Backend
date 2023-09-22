from django.forms import ModelForm
from .models.task import Task
from .models.comment import Comment

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']