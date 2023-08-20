from rest_framework.viewsets import ModelViewSet

from ..models import NodeMedia
from ..serializers import NodeMediaSerializer
from ..filters import NodeMediaFilter


class MindPalaceNodeMediaViewSet(ModelViewSet):

    queryset = NodeMedia.objects.all()
    serializer_class = NodeMediaSerializer
    filterset_class = NodeMediaFilter
