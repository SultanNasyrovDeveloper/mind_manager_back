from rest_framework import serializers

from mind_palace.palace import models
from mind_palace.node.models import PalaceNode

from .enums import MoveToPositionChoices


class UserMindPalaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserMindPalace
        fields = '__all__'


class PalaceStatisticsSerializer(serializers.Serializer):

    count = serializers.IntegerField()
    views = serializers.IntegerField()
    repetitions = serializers.IntegerField()
    size = serializers.IntegerField()
    average_rating = serializers.DecimalField(
        max_digits=3,
        decimal_places=1,
    )


class PalaceNodeMoveDataSerializer(serializers.Serializer):

    node = serializers.PrimaryKeyRelatedField(
        queryset=PalaceNode.objects.all()
    )
    target = serializers.PrimaryKeyRelatedField(
        queryset=PalaceNode.objects.all()
    )
    position = serializers.ChoiceField(
        choices=MoveToPositionChoices.choices()
    )