from django_filters import rest_framework as filters

from . import models


class LearningSessionFilterSet(filters.FilterSet):

    class Meta:
        model = models.UserLearningSession
        exclude = ('queue', 'additional_queue', 'repeated_nodes')
