from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from mind_palace.node.models import PalaceNode
from .enums import QueueGenerationStrategyEnum
from .managers import UserLearningSessionManager


class LearningSession(models.Model):
    """
    User learning learning_session.
    """
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
    current_node = models.ForeignKey(
        'node.PalaceNode',
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )

    start_datetime = models.DateTimeField(default=timezone.now)
    finish_datetime = models.DateTimeField(null=True, default=None)

    objects = UserLearningSessionManager()


class NodeLearningContext(models.Model):
    node = models.OneToOneField(
        'node.PalaceNode',
        on_delete=models.CASCADE,
        related_name='repetition_context'
    )
    easiness = models.DecimalField(max_digits=4, decimal_places=2, default=2.6)
    next_repetition = models.DateTimeField(
        auto_now_add=True
    )


@receiver(post_save, sender=PalaceNode)
def create_node_learning_context(created, instance, **kwargs):
    if created:
        NodeLearningContext.objects.create(node=instance)
