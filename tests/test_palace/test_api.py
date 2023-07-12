import pytest

from mind_palace.palace.models import PalaceNode

from ..test_node.factories import PalaceNodeFactory
from . import factories


@pytest.mark.django_db
def test_fetch_palace_list(user, api_client):
    palaces = []
    for i in range(20):
        root = PalaceNodeFactory()
        palaces.append(
            factories.PalaceFactory(user=user, root=root)
        )
    response = api_client.get()



@pytest.mark.django_db
def test_fetch_user_palace_detail():
    assert True
