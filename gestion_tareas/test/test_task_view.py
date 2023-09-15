from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from rest_framework.test import APITestCase

from ..models.task import Task
from ..serializers.task_serializers import TaskSerializer

class TaskAPITestCase(APITestCase):
    def setUp(self):
        # Configurar datos de prueba
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.task = Task.objects.create(user=self.user, title='Test Task')
        self.url = reverse('tasks')

    def test_get_single_task(self):
        response = self.client.get(reverse('task_detail', args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task') 

    def test_get_all_tasks(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_get_all_boards_empty(self):
        Task.objects.all().delete()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
