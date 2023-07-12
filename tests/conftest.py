import pytest
from rest_framework.test import APIClient
from mind_palace.user.models import User
from mind_palace.node import PalaceNode


@pytest.fixture(scope='module')
def logger():
    pass


@pytest.fixture(scope='module')
def api_client(user):
    client = APIClient()
    client.force_authenticate(user)
    return client


@pytest.fixture
def user():
    user = User(username='test', email='test@mail.ru')
    user.set_password('1Qetuwry')
    user.save()
    return user


@pytest.fixture
def user_mind_palace(user):
    return user.mind_palace


@pytest.fixture
def user_palace_root(user_mind_palace, faker):
    root = user_mind_palace.root
    for _ in range(10):
        PalaceNode.objects.create(parent=root, name=faker.pystr())
    return root
