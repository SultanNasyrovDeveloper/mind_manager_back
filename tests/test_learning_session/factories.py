from factory.django import DjangoModelFactory

from mind_palace.learning_session.models import LearningSession


class LearningSessionFactory(DjangoModelFactory):

    class Meta:
        model = LearningSession
