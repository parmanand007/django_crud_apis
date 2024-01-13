
from django_filters import rest_framework as filters
from .models import Animal


# We create filters for each field we want to be able to filter on
class AnimalFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    type = filters.CharFilter(lookup_expr='icontains')
    sound = filters.CharFilter(lookup_expr='icontains')
    created_at = filters.DateTimeFromToRangeFilter()
    updated_at = filters.DateTimeFromToRangeFilter()
    owner__username = filters.CharFilter(lookup_expr='icontains')
    owner__email = filters.CharFilter(lookup_expr='icontains')
    extra_information_key = filters.CharFilter(method='filter_extra_information_key')

    class Meta:
        model = Animal
        fields = ['name', 'type','sound','created_at', 'updated_at', 'owner__username', 'owner__email','extra_information_key']
    
    def filter_extra_information_key(self, queryset, name, value):
        # Filter based on keys in the extra_information JSON field
        return queryset.filter(extra_information__has_key=value)