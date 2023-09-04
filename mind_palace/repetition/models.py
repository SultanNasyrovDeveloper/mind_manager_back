from django.db import models


class NodeRepetition(models.Model):

    session = models.ForeignKey(
        'learning_session.LearningSession',
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
