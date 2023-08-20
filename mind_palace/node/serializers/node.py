from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .. import models
from mind_palace.learning.statistics.serializers import UserLearningStatisticsSerializer

from .media import NodeMediaSerializer
from .body import NodeBodySerializer


class NodeBriefInfoSerializer(serializers.ModelSerializer):
    """
    Serializes only nodes basic information.
    """

    class Meta:
        model = models.PalaceNode
        fields = ('id', 'name', 'parent')


class MindPalaceNodeSerializer(serializers.ModelSerializer):
    """
    Provide full mind palace node information.
    """
    ancestors = serializers.SerializerMethodField(read_only=True)
    statistics = UserLearningStatisticsSerializer(read_only=True)
    media = NodeMediaSerializer(many=True, read_only=True)
    body = serializers.PrimaryKeyRelatedField(required=False, read_only=True)

    class Meta:
        model = models.PalaceNode
        fields = (
            'id', 'ancestors', 'statistics', 'media', 'name', 'description',
            'children', 'parent', 'owner', 'body', 'level'
        )
        read_only_fields = ('children', )

    def get_ancestors(self, node):
        """
        Get list of ancestors.
        """
        return [
            {'id': ancestor.id, 'name': ancestor.name}
            for ancestor in node.get_ancestors(include_self=True)
        ]


class TreeNodeSerializer(serializers.Serializer):

    parent = serializers.PrimaryKeyRelatedField(read_only=True)
    id = serializers.IntegerField()
    name = serializers.CharField()
    children = serializers.ListField(child=RecursiveField(), source='get_children')
    statistics = UserLearningStatisticsSerializer(read_only=True)
