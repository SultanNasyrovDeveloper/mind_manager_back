from rest_framework import serializers

from mind_palace.learning.statistics import models


class UserLearningStatisticsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.NodeLearningStatistics
        fields = '__all__'
