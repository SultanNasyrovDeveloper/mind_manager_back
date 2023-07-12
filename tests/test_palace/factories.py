import factory.django as factory

from mind_palace.palace import models


class PalaceFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.UserMindPalace
