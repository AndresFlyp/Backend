from rest_framework import routers
from .api.user_api import UserViewSet
from .api.list_api import ListViewSet
from .api.task_api import TaskViewSet

router = routers.DefaultRouter()

router.register('user', UserViewSet, 'user')

router.register('list', ListViewSet, 'list')

router.register('task', TaskViewSet, 'task')

urlpatterns = router.urls
