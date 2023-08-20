import django_filters as filters

from ..core.filters import NumberInFilter
from . import models


class MindPalaceNodeFilter(filters.FilterSet):

    id_in = NumberInFilter(field_name='id', lookup_expr='in')
    id_not_in = NumberInFilter(exclude=True, field_name='id', lookup_expr='in')
    name = filters.CharFilter(lookup_expr='icontains')
    description = filters.CharFilter(lookup_expr='icontains')
    owner_id = filters.NumberFilter()

    class Meta:
        model = models.PalaceNode
        fields = ('name', 'description', 'owner_id')


class NodeMediaFilter(filters.FilterSet):

    class Meta:
        model = models.NodeMedia
        fields = ('title', 'description', 'type', 'node')