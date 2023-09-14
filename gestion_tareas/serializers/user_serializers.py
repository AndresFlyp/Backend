from rest_framework import serializers
from ..models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'created',)
        read_only_fields = ('created','last_update', 'password',)
        