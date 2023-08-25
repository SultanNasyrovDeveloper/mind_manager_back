from datetime import timedelta

from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

from .enums import QueueGenerationStrategyEnum
from .managers import UserLearningSessionManager


class LearningSession(models.Model):
    """
    User learning learning_session.
    """
    # basic
    is_active = models.BooleanField(default=False)
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, related_name='learning_sessions',
    )

    targets = models.ManyToManyField(
        'node.PalaceNode',
        default=list,
        related_name='learning_sessions'
    )
    queue_generation_strategy = models.IntegerField(
        choices=QueueGenerationStrategyEnum.choices(),
        default=QueueGenerationStrategyEnum.outdated_first
    )
    queue = ArrayField(models.IntegerField(), default=list)

    # time marks
    start_datetime = models.DateTimeField(default=timezone.now)
    finish_datetime = models.DateTimeField(null=True, default=None)
    last_repetition_datetime = models.DateTimeField(default=timezone.now)

    objects = UserLearningSessionManager()

    def is_expired(self):
        is_active = self.is_active
        is_expired = self.last_repetition_datetime < timezone.now() - timedelta(hours=1)
        return is_active and is_expired


class NodeRepetition(models.Model):

    session = models.ForeignKey(
        LearningSession,
        on_delete=models.CASCADE,
        related_name='repetitions'
    )
    node = models.ForeignKey(
        'node.PalaceNode',
        on_delete=models.CASCADE,
        related_name='repetitions'
    )
    rating = models.PositiveSmallIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
