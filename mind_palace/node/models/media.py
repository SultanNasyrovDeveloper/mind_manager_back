from django.db import models

from mind_palace.node.enums import NodeMediaTypeEnum


class NodeMedia(models.Model):
    """
    Responsible for storing one media object with image or other king of media.

    Currently, only image or icon or youtube video media available.
    """
    node = models.ForeignKey(
        'node.PalaceNode',
        on_delete=models.CASCADE,
        related_name='media'
    )
    type = models.PositiveSmallIntegerField(
        choices=NodeMediaTypeEnum.choices(),
        default=NodeMediaTypeEnum.not_set,
    )
    title = models.CharField(max_length=500, null=True, default=None)
    description = models.TextField(null=True, default=None)
    config = models.JSONField(default=dict)