import factory.django as factory
from faker import Faker

from mind_palace.node import models

faker = Faker()


class PalaceNodeFactory(factory.DjangoModelFactory):

    user = 1
    name = faker.pystr()
    description = faker.pystr()

    class Meta:
        model = models.PalaceNode
