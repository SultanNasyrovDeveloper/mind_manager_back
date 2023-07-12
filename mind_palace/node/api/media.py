from rest_framework.viewsets import ModelViewSet

from mind_palace.node.models import NodeMedia
from mind_palace.node.serializers import NodeMediaSerializer


class MindPalaceNodeMediaViewSet(ModelViewSet):

    queryset = NodeMedia.objects.all()
    serializer_class = NodeMediaSerializer
