from rest_framework import serializers

from mind_palace.node.models import PalaceNode
from mind_palace.learning.session import models
from mind_palace.learning.strategy.enums import MindPalaceLearningStrategiesEnum


class UserLearningSessionSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    targets = serializers.PrimaryKeyRelatedField(
        queryset=PalaceNode.objects.all(),
        many=True
    )
    strategy_name = serializers.ChoiceField(
        choices=MindPalaceLearningStrategiesEnum.choices(),
    )
    current = serializers.SerializerMethodField(
        read_only=True,
        method_name='get_current'
    )

    class Meta:
        model = models.UserLearningSession
        fields = (
            'id', 'is_active', 'strategy_name', 'targets', 'user', 'current',
            'start_datetime', 'finish_datetime', 'last_repetition_datetime',
        )
        read_only_fields = (
            'id', 'is_active', 'start_datetime', 'finish_datetime', 'last_repetition_datetime',
            'user',b'current', 'targets', 'strategy_name'
        )

    def get_current(self, session):
        if type(session) != models.UserLearningSession:
            session = models.UserLearningSession(
                **{
                    key: value
                    for key, value
                    in session.items()
                    if key not in ('targets', )
                }
            )
        return session.queue_manager.current()

    def create(self, validated_data):
        session = super().create(validated_data)
        models.LearningSessionStatistics.objects.create(session=session)
        return session


class NodeStudyDataSerializer(serializers.Serializer):

    node = serializers.IntegerField()
    rating = serializers.IntegerField(min_value=1, max_value=6)
