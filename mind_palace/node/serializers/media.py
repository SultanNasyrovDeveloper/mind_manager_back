from rest_framework import serializers

from mind_palace.node import models


class NodeMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.NodeMedia
        exclude = ('image', )
