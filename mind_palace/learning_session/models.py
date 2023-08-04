from datetime import timedelta

from django.db import models
from django.dispatch import receiver
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

from .enums import QueueGenerationStrategiesEnum
from .managers import UserLearningSessionManager


class UserLearningSession(models.Model):
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
        choices=QueueGenerationStrategiesEnum.choices(),
        default=QueueGenerationStrategiesEnum.outdated_first
    )
    queue = ArrayField(models.IntegerField(), default=list)
    repeated_nodes = ArrayField(models.IntegerField(), default=list)

    # time marks
    start_datetime = models.DateTimeField(default=timezone.now)
    finish_datetime = models.DateTimeField(null=True, default=None)
    last_repetition_datetime = models.DateTimeField(default=timezone.now)

    objects = UserLearningSessionManager()

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
