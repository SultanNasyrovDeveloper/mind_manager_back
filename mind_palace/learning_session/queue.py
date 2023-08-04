import random
from django.utils import timezone

from ..node.models import PalaceNode


class QueueGenerationStrategy:

    def generate(self, targets: list):
        raise NotImplementedError


class TotalRandomQueueGeneration(QueueGenerationStrategy):

    def generate(self, targets):
        queue = []
        for target in targets:
            queue.extend(list(
                target.get_descendants(include_self=True).values_list('id', flat=True)
            ))
        random.shuffle(queue)
        return queue


class OutdatedFirstQueueGeneration(QueueGenerationStrategy):

    def generate(self, targets):
        # filter targets descendants by next repetition
        nodes_to_queue = []
        for target in targets:
            nodes_to_queue.extend(list(
                target.get_descendants(include_self=True)
                .values_list('id', flat=True)
            ))
        return list(
            PalaceNode.objects
            .filter(statistics__next_repetition__lte=timezone.now())
            .values_list('id', flat=True)
        )


# class LastRepeatedFirstQueueGenerationStrategy(QueueGenerationStrategy): pass


def get_queue_generation_strategy(strategy_id: int):
    return {
        1: TotalRandomQueueGeneration,
        2: OutdatedFirstQueueGeneration
    }[strategy_id]
