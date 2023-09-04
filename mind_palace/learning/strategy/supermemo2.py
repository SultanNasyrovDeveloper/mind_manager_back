from dataclasses import dataclass
from datetime import timedelta, datetime

from decimal import Decimal

from mind_palace.learning.strategy.base import BaseLearningStrategy


@dataclass
class StudyNodeContext:
    positive_repetitions_in_row: int
    easiness: Decimal
    last_repetition: datetime


@dataclass
class StudyNodeResult:
    easiness: Decimal
    next_repetition: datetime


class SuperMemo2LearningStrategy(BaseLearningStrategy):

    def study_node(self, rating: int, context: StudyNodeContext) -> StudyNodeResult:
        """
        Handle node repetition using supermemo2 strategy.

        https://www.supermemo.com/ru/archives1990-2015/english/ol/sm2
        This is implementation of algorithm described in the link.
        Repetition strategy calculates optimal next repetition datetime of some data item based on
        user repetition rating(subjective repetition quality evaluation).
        """
        interval = 1
        result = StudyNodeResult(
            easiness=context.easiness,
            next_repetition=context.last_repetition + timedelta(days=1)
        )
        if rating < 3:  # means user rated this repetition as not positive
            result.easiness = context.easiness

        else:
            q = rating
            new_easiness = context.easiness + Decimal(
                (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
            )
            result.easiness = new_easiness.quantize(Decimal('1.0'))

            if context.positive_repetitions_in_row == 0:
                interval = 1  # if this is first positive repetition repeat this node tomorrow again
            elif context.positive_repetitions_in_row == 1:
                context.interval = 4  # According to supermemo2 should be 6 days
            else:
                interval = round(context.interval * context.easiness, 1)

        result.next_repetition = (
            context.last_repetition + timedelta(days=float(interval))
        )
        return result
