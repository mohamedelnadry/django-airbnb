from django.template.defaultfilters import title
import django_filters
from .models import Property

class PropertyFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Property
        fields = ['title', 'place' ,'category','min_price', 'max_price']


