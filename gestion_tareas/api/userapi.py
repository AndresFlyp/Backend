from ..models.user import User
from rest_framework import viewsets, permissions
from ..serializers.user_serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny] 
    serializer_class = UserSerializer
