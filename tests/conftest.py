import pytest

from rest_framework.test import APIClient

from mind_palace.user.models import User
from .constants import TEST_USER_USERNAME, TEST_USER_EMAIL, TEST_USER_PASSWORD
from .test_node.factories import PalaceNodeFactory


@pytest.fixture
def user():
    user = User(username=TEST_USER_USERNAME, email=TEST_USER_EMAIL)
    user.set_password(TEST_USER_PASSWORD)
    user.save()
    for _ in range(10):
        PalaceNodeFactory(parent=user.mind_palace.root)
    return user


@pytest.fixture
def api_client(user):
    client = APIClient()
    client.force_authenticate(user)
    return client
