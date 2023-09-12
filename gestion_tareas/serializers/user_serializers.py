from rest_framework import serializers
from ..models import user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user.User
        fields = ('email', 'username', 'password', 'created',)
        read_only_fields = ('created','last_update',)
        