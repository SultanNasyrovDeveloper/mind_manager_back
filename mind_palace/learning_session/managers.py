from datetime import timedelta

from django.conf import settings
from django.db import models
from django.utils import timezone

from mind_palace.node.models import PalaceNode
from ..learning.strategy.supermemo2 import SuperMemo2LearningStrategy, StudyNodeResult
from .queue import OutdatedFirstQueueGeneration
from .utils import prepare_node_learning_context


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
        session.current_node_id = OutdatedFirstQueueGeneration.next(targets)
        session.save()
        session.targets.set([target.id for target in targets])
        return session

    def study_node(self, node: int, rating: int) -> StudyNodeResult:
        """x
        Handle study node by user.
        """
        node = PalaceNode.objects.get(id=node)
        learning_context = prepare_node_learning_context(node)
        learning_strategy = SuperMemo2LearningStrategy()
        result = learning_strategy.study_node(rating=rating, context=learning_context)
        return result

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
            initial_queryset(QuerySet): Initial sessions queryset.
            query_params: Django like query params will be passed into manager's filter method.
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
