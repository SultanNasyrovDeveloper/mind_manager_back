from django.db import models

from django.dispatch import receiver
from django.utils import timezone

from mind_palace.learning.statistics.enums import UserNodeLearningStatusEnum
from mind_palace.node.models import PalaceNode


class NodeLearningStatistics(models.Model):

    node = models.OneToOneField(
        'node.PalaceNode', on_delete=models.CASCADE, related_name='statistics',
    )

    status = models.CharField(
        max_length=100, choices=UserNodeLearningStatusEnum.choices(),
        default=UserNodeLearningStatusEnum.rookie,
    )
    interval = models.IntegerField(default=0)
    repetitions = models.BigIntegerField(default=0)
    views = models.BigIntegerField(default=0)
    positive_repetitions_in_row = models.BigIntegerField(default=0)
    easiness = models.DecimalField(max_digits=4, decimal_places=2, default=2.6)
    average_rate = models.DecimalField(max_digits=2, decimal_places=1, default=0)

    last_repetition = models.DateTimeField(default=timezone.now)
    next_repetition = models.DateTimeField(default=timezone.now)
    last_view = models.DateTimeField(default=timezone.now)


@receiver(models.signals.post_save, sender=PalaceNode)
def create_palace_node(sender, instance, created, **kwargs):
    if created:
        NodeLearningStatistics.objects.create(node=instance)
