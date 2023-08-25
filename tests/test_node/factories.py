import factory
from factory.django import DjangoModelFactory

from mind_palace.node.models import PalaceNode


class PalaceNodeFactory(DjangoModelFactory):

    name = factory.Faker('name')
    description = factory.Faker('paragraph')

    class Meta:
        model = PalaceNode
