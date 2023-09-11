from rest_framework import serializers
from ..models import user

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = user.User
        fields = '__all__'