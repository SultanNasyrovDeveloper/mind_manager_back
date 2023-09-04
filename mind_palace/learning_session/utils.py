from django.utils import timezone
from mind_palace.node.models import PalaceNode
from ..learning.strategy.supermemo2 import StudyNodeContext


def prepare_node_learning_context(node: PalaceNode) -> StudyNodeContext:
    # fetch 3 last repetitions
    positive_repetitions_in_row = 0
    last_three_repetitions = node.repetitions.order_by('date')[:3]
    if last_three_repetitions:
        for repetition in last_three_repetitions:
            if repetition.rating > 3: positive_repetitions_in_row += 1
    return StudyNodeContext(
        positive_repetitions_in_row=positive_repetitions_in_row,
        easiness=node.repetition_context.easiness,
        last_repetition=(
            last_three_repetitions.first().date
            if last_three_repetitions
            else timezone.now()
        ),
    )