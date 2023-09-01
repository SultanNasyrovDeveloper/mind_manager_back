import pytest
import json

from django.urls import reverse
from rest_framework import status

from mind_palace.learning_session.enums import QueueGenerationStrategyEnum
from mind_palace.learning_session.models import LearningSession, NodeRepetition
from mind_palace.learning_session.serializers import LearningSessionSerializer
from .factories import LearningSessionFactory


@pytest.mark.django_db
def test_get_learning_session(api_client, user):
    learning_session = LearningSessionFactory(user=user)
    learning_session.targets.add(user.mind_palace.root.id)

    url = reverse('learning_session-detail', args=[learning_session.id])
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data == LearningSessionSerializer(learning_session).data


@pytest.mark.django_db
def test_get_learning_session_list(api_client, user):
    number_of_learning_sessions = 25
    learning_sessions = []
    for _ in range(number_of_learning_sessions):
        session = LearningSessionFactory(user=user)
        session.targets.add(user.mind_palace.root)
        learning_sessions.append(session)

    url = reverse('learning_session-list')
    response = api_client.get(url, {'limit': number_of_learning_sessions})

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get('count', 0) == number_of_learning_sessions

    expected_response_data = [
        LearningSessionSerializer(session).data
        for session in learning_sessions
    ]
    assert response.data.get('results', []) == expected_response_data


@pytest.mark.django_db
def test_get_my_active_learning_session(api_client, user):
    url = reverse('learning_session-active_session')
    response = api_client.get(url)
    assert not response.data

    active_session = LearningSessionFactory(is_active=True, user=user)
    active_session.targets.add(user.mind_palace.root)

    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == LearningSessionSerializer(active_session).data


@pytest.mark.django_db
def test_start_learning_session(api_client, user):
    start_session_data = {
        'targets': [user.mind_palace.root.id],
        'user': user.id,
        'queue_generation_strategy': QueueGenerationStrategyEnum.outdated_first
    }
    url = reverse('learning_session-start')
    response = api_client.post(
        url,
        json.dumps(start_session_data),
        content_type='application/json'
    )
    assert response.status_code == status.HTTP_201_CREATED
    new_session_id = response.data.get('id', None)
    assert new_session_id
    target_session = LearningSession.objects.get(id=new_session_id)
    assert target_session
    assert response.data == LearningSessionSerializer(target_session).data
    response = api_client.post(
        url,
        json.dumps(start_session_data),
        content_type='application/json'
    )
    assert response.status_code == status.HTTP_409_CONFLICT


@pytest.mark.django_db
def test_record_repetition(api_client, user):
    learning_session = LearningSessionFactory(user=user, is_active=True)
    learning_session.targets.set([user.mind_palace.root.id])
    repetition_data = {
        'node': user.mind_palace.root.id,
        'rating': 5
    }
    url = reverse('learning_session-record_repetition', args=[learning_session.id])
    response = api_client.post(
        url,
        json.dumps(repetition_data),
        content_type='application/json'
    )
    assert status.is_success(response.status_code)
    assert NodeRepetition.objects.filter(
        session_id=learning_session.id,
        node=user.mind_palace.root.id,
        rating=5
    ).exists()


@pytest.mark.django_db
def test_finish_learning_session(api_client, user):
    learning_session = LearningSessionFactory(user=user, is_active=True)
    learning_session.targets.set([user.mind_palace.root.id])
    url = reverse('learning_session-finish', args=[learning_session.id])
    response = api_client.post(url)
    assert response.status_code == status.HTTP_200_OK
    finished_session = LearningSession.objects.get(id=learning_session.id)
    assert not finished_session.is_active