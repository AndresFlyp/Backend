from rest_framework import routers
from .api.userapi import UserViewSet
from .api.listapi import ListViewSet
from .api.taskapi import TaskViewSet

router = routers.DefaultRouter()

router.register('user', UserViewSet, 'user')

router.register('list', ListViewSet, 'list')

router.register('task', TaskViewSet, 'task')

urlpatterns = router.urls
