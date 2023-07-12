from datetime import timedelta

from django.db import models
from django.dispatch import receiver
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

from mind_palace.learning.session.managers import UserLearningSessionManager
from mind_palace.learning.session.queue import LearningQueueManager
from mind_palace.learning.strategy.enums import MindPalaceLearningStrategiesEnum
from mind_palace.learning.strategy.factory import UserLearningStrategyFactory


class UserLearningSession(models.Model):
    """
    User learning session.
    """
    # basic
    is_active = models.BooleanField(default=False)
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, related_name='learning_sessions',
    )
    strategy_name = models.CharField(
        max_length=1000, choices=MindPalaceLearningStrategiesEnum.choices(),
        default=MindPalaceLearningStrategiesEnum.supermemo_2,
    )
    targets = models.ManyToManyField(
        'node.PalaceNode',
        default=list,
        related_name='learning_sessions'
    )

    # nodes
    queue = ArrayField(models.IntegerField(), default=list)
    additional_queue = ArrayField(models.IntegerField(), default=list)
    repeated_nodes = ArrayField(models.IntegerField(), default=list)

    # time marks
    start_datetime = models.DateTimeField(default=timezone.now)
    finish_datetime = models.DateTimeField(null=True, default=None)
    last_repetition_datetime = models.DateTimeField(default=timezone.now)

    objects = UserLearningSessionManager()

    @property
    def learning_strategy(self):
        return UserLearningStrategyFactory.create(self.strategy_name)

    @property
    def queue_manager(self):
        return LearningQueueManager(self)

    def is_expired(self):
        is_active = self.is_active
        is_expired = self.last_repetition_datetime < timezone.now() - timedelta(hours=1)
        return is_active and is_expired


class LearningSessionStatistics(models.Model):

    session = models.OneToOneField(
        UserLearningSession,
        on_delete=models.CASCADE,
        related_name='statistics'
    )
    average_rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=0
    )
    repetitions = models.IntegerField(default=0)


@receiver(signal=models.signals.post_save, sender=UserLearningSession)
def create_learning_session_statistics(sender, instance, created, **kwargs):
    if created:
        LearningSessionStatistics.objects.create(session=instance)
