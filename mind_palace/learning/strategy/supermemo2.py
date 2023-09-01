from datetime import timedelta
from decimal import Decimal
from django.utils import timezone

from mind_palace.learning.strategy.base import BaseLearningStrategy
from ..statistics.models import NodeLearningStatistics


class SuperMemo2LearningStrategy(BaseLearningStrategy):

    def study_node(self, node_learning_stats: NodeLearningStatistics, rating: int):
        """
        Handle node repetition using supermemo2 strategy.

        https://www.supermemo.com/ru/archives1990-2015/english/ol/sm2
        This is implementation of algorithm described in the link.
        Repetition strategy calculates optimal next repetition datetime of some data item based on
        user repetition rating(subjective repetition quality evaluation).
        """

        if rating < 3:  # means user rated this repetition as not positive
            node_learning_stats.positive_repetitions_in_row = 0
            node_learning_stats.easiness = node_learning_stats.easiness
            node_learning_stats.interval = 1

        else:
            q = rating
            new_easiness = node_learning_stats.easiness + Decimal(
                (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
            )
            node_learning_stats.easiness = new_easiness.quantize(Decimal('1.0'))

            if node_learning_stats.positive_repetitions_in_row == 0:
                # if this is first positive repetition repeat this node tomorrow again
                node_learning_stats.interval = 1

            elif node_learning_stats.positive_repetitions_in_row == 1:
                # According to supermemo2 must be 6 days
                node_learning_stats.interval = 4
            else:
                node_learning_stats.interval = round(
                    node_learning_stats.interval * node_learning_stats.easiness, 1
                )

            node_learning_stats.positive_repetitions_in_row += 1

        node_learning_stats.next_repetition = (
            node_learning_stats.last_repetition + timedelta(days=float(node_learning_stats.interval))
        )
        node_learning_stats.last_repetition = timezone.now()
        node_learning_stats.average_rate = (
            ((node_learning_stats.repetitions * node_learning_stats.average_rate) + rating) /
            (node_learning_stats.repetitions + 1)
        )
        node_learning_stats.repetitions += 1
        node_learning_stats.save()
