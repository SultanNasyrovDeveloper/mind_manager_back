from datetime import datetime, timedelta, timezone

import pytest

from mind_palace.learning.session import models, managers
from mind_palace.learning.strategy.enums import MindPalaceLearningStrategiesEnum


@pytest.mark.django_db
def test_finish_bulk(user, user_mind_palace):
    pass


@pytest.mark.django_db
def test_finish_expired(user, user_mind_palace):
    expired_sessions = []
    for index in range(20):
        session = models.UserLearningSession.objects.create(
            is_active=True,
            user_id=user.id,
            strategy_name=MindPalaceLearningStrategiesEnum.supermemo_2,
            start_datetime=datetime.utcnow() - timedelta(days=100, hours=index),
            last_repetition_datetime=datetime.utcnow() - timedelta(days=100, minutes=index)
        )
        session.targets.set([user_mind_palace.root])
        expired_sessions.append(session)
    active_session = models.UserLearningSession.objects.create(
        is_active=True,
        user_id=user.id,
        strategy_name=MindPalaceLearningStrategiesEnum.supermemo_2,
        start_datetime=datetime.utcnow(),
        last_repetition_datetime=datetime.utcnow()
    )
    models.UserLearningSession.objects.finish_expired(user=user.id)
    active_session_ids = list(models.UserLearningSession.objects.filter(
        is_active=True, user_id=user.id
    ).values_list('id', flat=True))
    assert active_session_ids == [active_session.id]
