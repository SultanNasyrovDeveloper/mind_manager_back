from djoser.serializers import (
    UserCreateSerializer as DjoserUserCreateSerializer
)
from rest_framework import serializers

from . import models


class UserCreateSerializer(DjoserUserCreateSerializer):

    class Meta(DjoserUserCreateSerializer.Meta):
        model = models.User
        fields = ('id', 'email', 'password')


class UserSerializer(serializers.ModelSerializer):

    mind_palace = serializers.IntegerField(source='mind_palace.root.id')

    class Meta:
        model = models.User
        exclude = ('password', )


