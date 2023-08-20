from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from mind_palace.learning_session import filters

from . import exceptions, models, permissions, serializers


class LearningSessionViewSet(ModelViewSet):
    # TODO: Add permission to user actions
    queryset = models.UserLearningSession.objects.all()
    serializer_class = serializers.UserLearningSessionSerializer
    filterset_class = filters.LearningSessionFilterSet
    permission_classes = [permissions.IsSessionOwner]

    def retrieve(self, request, *args, **kwargs):
        session = self.get_object()
        if session.is_expired():
            models.UserLearningSession.objects.finish(session)
        return Response(self.get_serializer_class()(session).data)

    @action(detail=False, methods=('GET', ))
    def active_session(self, request, *args, **kwargs):
        response_data = None
        models.UserLearningSession.objects.finish_expired(user_id=request.user.id)
        target_session = self.queryset.filter(user=request.user.id, is_active=True).first()
        if target_session:
            response_data = self.serializer_class(target_session).data
        return Response(response_data)

    @action(detail=False, methods=('POST', ))
    def start(self, request, *args, **kwargs):
        """
        Start new learning learning_session.
        """
        models.UserLearningSession.objects.finish_expired(user_id=request.user.id)
        active_sessions = models.UserLearningSession.objects.filter(
            is_active=True,
            user_id=request.user.id
        )
        if active_sessions:
            raise exceptions.ActiveSessionAlreadyExistsError()
        session_data = dict(request.data)
        session_data['user'] = request.user.id
        serializer = self.serializer_class(data=session_data)
        serializer.is_valid(raise_exception=True)
        new_session = serializer.save()
        return Response(self.serializer_class(new_session).data)

    @action(detail=True, methods=('POST', ))
    def regenerate_queue(self, request, *args, **kwargs):
        # Run generate queue logic
        pass

    @action(detail=True, methods=('POST', ))
    def record_repetition(self, request, *args, **kwargs):
        """
        Handle node studying.
        """
        session = self.get_object()
        serializer = serializers.NodeStudyDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        models.UserLearningSession.objects.study_node(session, **serializer.validated_data)
        return Response(self.serializer_class(session).data)

    @action(detail=True, methods=('POST',))
    def finish(self, request, *args, **kwargs):
        """
        Finish learning_session.
        """
        models.UserLearningSession.objects.finish(self.get_object())
        return Response()
