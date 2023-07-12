from rest_framework.viewsets import ModelViewSet

from .. import models, serializers, permissions


class NodeBodyViewSet(ModelViewSet):
    queryset = models.NodeBody.objects.all()
    serializer_class = serializers.NodeBodySerializer
    permission_classes = [permissions.IsNodeBodyOwner]
