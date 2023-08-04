from django_filters.filters import BaseInFilter, NumberFilter


class NumberInFilter(BaseInFilter, NumberFilter):
    pass