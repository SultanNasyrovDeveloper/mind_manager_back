import django_filters as filters

from mind_palace.node import models


class MindPalaceNodeFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    description = filters.CharFilter(lookup_expr='icontains')
    owner_id = filters.NumberFilter()

    class Meta:
        model = models.PalaceNode
        fields = ('name', 'description', 'owner_id')
