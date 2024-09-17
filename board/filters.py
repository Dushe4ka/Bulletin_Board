import django_filters
from .models import Advertisement


class AdvertisementFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Название объявления')

    class Meta:
        model = Advertisement
        fields = ['title']
