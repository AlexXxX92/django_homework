
from django_filters import rest_framework as filters, DateFromToRangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = filters.DateFromToRangeFilter()
    creator = filters.CharFilter()
    status = filters.CharFilter()
    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        fields = ('created_at', 'creator', 'status')
