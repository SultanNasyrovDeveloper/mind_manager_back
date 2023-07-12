from django.db import models
from django.contrib.postgres.fields import ArrayField

from mind_palace.node.enums import NodeBodyTypeEnum


class NodeBody(models.Model):

    node = models.OneToOneField(
        'node.PalaceNode',
        on_delete=models.CASCADE,
        related_name='body'
    )
    type = models.CharField(
        max_length=50,
        choices=NodeBodyTypeEnum.choices(),
        default=NodeBodyTypeEnum.TEXT
    )
    meta = models.JSONField(default=dict)
    fields = ArrayField(models.CharField(max_length=1000), default=list)
    data = models.JSONField(default=list)
    size = models.PositiveIntegerField(default=0)
