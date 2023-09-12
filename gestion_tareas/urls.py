from rest_framework import routers
from .api.userapi import UserViewSet
from .api.listapi import ListViewSet

router = routers.DefaultRouter()

router.register('api/user', UserViewSet, 'user')

router.register('api/list', ListViewSet, 'list')

urlpatterns = router.urls
