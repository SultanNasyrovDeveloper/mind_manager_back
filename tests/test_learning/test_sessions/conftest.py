import pytest

from mind_palace.user.models import User
from mind_palace.node import PalaceNode
from mind_palace.learning_session import models
from mind_palace.learning.strategy.enums import LearningStrategiesEnum


@pytest.fixture(scope='function')
def learning_session(
        user: User,
        user_palace_root: PalaceNode
) -> models.UserLearningSession:
    session = models.UserLearningSession.objects.start(
        targets=[user_palace_root],
        strategy_name=LearningStrategiesEnum.supermemo_2,
    )
    return session


@pytest.fixture(scope='function')
def learning_session_factory(user: User):
    return lambda initial, count = 1: [
        models.UserLearningSession.objects.create(
            is_active=False,
            **initial
        )
        for index in range(count)
    ]
