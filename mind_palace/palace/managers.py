from django.db.models import Manager, Count, Sum, Avg

from mind_palace.learning.statistics.models import NodeLearningStatistics


class PalaceManger(Manager):

    def get_subtree_statistics(self, root):
        nodes_qs = root.get_descendants(include_self=True)
        node_statistics = NodeLearningStatistics.objects.filter(
            id__in=list(nodes_qs.values_list('id', flat=True))
        )
        return {
            'root': root.id,
            'count': nodes_qs.count(),
            'size': nodes_qs.select_related('body').aggregate(size=Sum('body__size'))['size'],
            **node_statistics.aggregate(
                views=Sum('views'),
                repetitions=Sum('repetitions'),
                average_rating=Avg('average_rate')
            )
        }

