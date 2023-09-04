from typing import Any

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet

from mind_palace.learning_session import filters
from mind_palace.repetition.models import NodeRepetition
from . import exceptions, models, permissions, serializers


class LearningSessionViewSet(ModelViewSet):
    # TODO: Add permission to user actions
    queryset = models.LearningSession.objects.all()
    serializer_class = serializers.LearningSessionSerializer
    filterset_class = filters.LearningSessionFilterSet
    permission_classes = [permissions.IsSessionOwner]

    def retrieve(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        session = self.get_object()
        return Response(self.get_serializer_class()(session).data)

    @action(detail=False, methods=('GET', ), url_name='active_session')
    def active_session(self, request, *args, **kwargs):
        response_data = None
        target_session = self.queryset.filter(user=request.user.id, is_active=True).first()
        if target_session:
            response_data = self.serializer_class(target_session).data
        return Response(response_data)

    @action(
        detail=False,
        methods=('POST', ),
        url_name='start',
    )
    def start(self, request, *args, **kwargs):
        """
        Start new learning learning_session.
        """
        active_sessions = models.LearningSession.objects.filter(
            is_active=True,
            user_id=request.user.id
        )
        if active_sessions:
            raise exceptions.ActiveSessionAlreadyExistsError()
        session_data = dict(request.data)
        session_data['user'] = request.user.id
        serializer = self.serializer_class(data=session_data)
        serializer.is_valid(raise_exception=True)
        new_session = models.LearningSession.objects.start(**serializer.validated_data)
        return Response(
            self.serializer_class(new_session).data,
            status=status.HTTP_201_CREATED
        )

    @action(detail=True, methods=('POST', ), url_name='record_repetition')
    def record_repetition(self, request, *args, **kwargs):
        """
        Handle node studying.
        """
        session = self.get_object()
        serializer = serializers.NodeStudyDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        models.LearningSession.objects.study_node(**serializer.validated_data)
        NodeRepetition.objects.create(
            session=session,
            node_id=serializer.validated_data.get('node'),
            rating=serializer.validated_data.get('rating'),
        )
        return Response(
            self.serializer_class(session).data,
            status=status.HTTP_201_CREATED
        )

    @action(detail=True, methods=('POST', ), url_name='finish')
    def finish(self, request, *args, **kwargs):
        """
        Finish learning_session.
        """
        models.LearningSession.objects.finish(self.get_object())
        return Response(status=status.HTTP_200_OK)
