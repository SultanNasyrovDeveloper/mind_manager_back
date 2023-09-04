import random

from ..node.models import PalaceNode


class QueueGenerationStrategy:

    def generate(self, targets: list):
        raise NotImplementedError


class TotalRandomQueueGeneration(QueueGenerationStrategy):

    def generate(self, targets):
        queue = []
        for target in targets:
            queue.extend(list(
                target.get_descendants(include_self=True)
                .order_by('repetition_context.next_repetition')
                .values_list('id', flat=True)
            ))
        random.shuffle(queue)
        return queue

    def next(self, targets): ...


class OutdatedFirstQueueGeneration(QueueGenerationStrategy):

    @staticmethod
    def next(targets):
        # filter targets descendants by next repetition
        nodes_to_queue = []
        for target in targets:
            nodes_to_queue.extend(list(
                target.get_descendants(include_self=True)
                .values_list('id', flat=True)
            ))
        return PalaceNode.objects\
            .filter(id__in=nodes_to_queue)\
            .order_by('repetition_context__next_repetition')\
            .values_list('id', flat=True)\
            .first()

# class LastRepeatedFirstQueueGenerationStrategy(QueueGenerationStrategy): pass


def get_queue_generation_strategy(strategy_id: int):
    return {
        1: TotalRandomQueueGeneration,
        2: OutdatedFirstQueueGeneration
    }[strategy_id]
