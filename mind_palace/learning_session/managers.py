from datetime import timedelta

from django.conf import settings
from django.db import models
from django.utils import timezone

from mind_palace.node import models as node_models
from mind_palace.learning.statistics.models import NodeLearningStatistics

from ..learning.strategy.supermemo2 import SuperMemo2LearningStrategy
from .queue import get_queue_generation_strategy


class UserLearningSessionManager(models.Manager):

    def start(self, **session_data):
        """
        Start new learning learning_session.

        Args:
            session_data: Field values for new learning_session that will be created.
            Must be validated before. Use UserLearningSessionSerializer.
        """
        targets = session_data.pop('targets')
        session = self.model(**session_data, is_active=True)
        queue_strategy = get_queue_generation_strategy(session.queue_generation_strategy)
        session.queue = queue_strategy().generate(list(targets))
        session.save()
        for target in targets:
            session.targets.add(target)
        return session

    def study_node(self, session, **kwargs):
        """
        Handle study node by user.
        """
        node_id = kwargs.pop('node')
        node_learning_stats = NodeLearningStatistics.objects.get(node_id=node_id)
        learning_strategy = SuperMemo2LearningStrategy()
        learning_strategy.study_node(node_learning_stats, **kwargs)
        session.statistics.average_rating = round((
            (session.statistics.average_rating * (session.statistics.repetitions - 1) + kwargs.get('rating'))
            / session.statistics.repetitions if session.statistics.repetitions else 1
        ), 1)
        session.last_repetition_datetime = timezone.now()
        if node_id in session.queue_manager:
            session.queue_manager.remove(node_id)
        session.repeated_nodes.append(node_id)
        session.save()
        return session

    def finish(self, session):
        """
        Finish given learning_session.
        """
        session.queue = list()
        session.finish_datetime = timezone.now()
        session.is_active = False
        session.save()
        return session

    def finish_bulk(self, sessions):
        """
        Finish all sessions in given queryset.

        Args:
            sessions: Session queryset.
        """
        sessions.update(
            is_active=False,
            queue=list(),
            finish_datetime=timezone.now()
        )

    def finish_expired(self, initial_queryset=None, **query_params) -> None:
        """
        Finish all expired learning_session filtered by given query params.

        First filter all learning_session by given query parameters then close all expired learning_session among them.

        Args:
            initial_queryset: Initial sessions queryset.
            query_params: Django like query params will be put in manager filter method.
        """
        initial_queryset = initial_queryset or self.all()
        expired_sessions = initial_queryset.filter(
            **query_params,
            is_active=True,
            last_repetition_datetime__lt=timezone.now() - timedelta(
                minutes=settings.USER_LEARNING_SESSION_EXPIRE
            )
        )
        self.finish_bulk(expired_sessions)
