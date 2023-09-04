from rest_framework import serializers

from mind_palace.node.models import PalaceNode
from mind_palace.learning_session import models
from mind_palace.user.models import User


class LearningSessionSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    targets = serializers.PrimaryKeyRelatedField(
        queryset=PalaceNode.objects.all(),
        many=True
    )
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
    )

    class Meta:
        model = models.LearningSession
        fields = (
            'id', 'is_active', 'targets', 'user', 'current_node', 'queue_generation_strategy',
            'start_datetime', 'finish_datetime'
        )
        read_only_fields = (
            'id', 'is_active', 'start_datetime', 'finish_datetime',
            'user', 'current_node', 'targets'
        )


class NodeStudyDataSerializer(serializers.Serializer):

    node = serializers.IntegerField()
    rating = serializers.IntegerField(min_value=1, max_value=6)
