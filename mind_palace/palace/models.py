from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from mind_palace.user.models import User
from mind_palace.node.enums import NodeBodyTypeEnum
from mind_palace.node.models import PalaceNode

from . import managers


class UserMindPalace(models.Model):
    root = models.OneToOneField(
        'node.PalaceNode',
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        blank=True,
        related_name='mind_palace'
    )

    user = models.OneToOneField(
        'user.User',
        on_delete=models.CASCADE,
        related_name='mind_palace'
    )

    objects = managers.PalaceManger()


@receiver(post_save, sender=User)
def create_user_mind_palace(instance, created, **kwargs):
    if created:
        root_node = PalaceNode.objects.create(
            name='My palace',
            owner=instance,
            body_data={'type': NodeBodyTypeEnum.TEXT}
        )
        UserMindPalace.objects.create(user=instance, root=root_node)

