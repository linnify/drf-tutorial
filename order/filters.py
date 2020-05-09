from django_filters import CharFilter
from django_filters.rest_framework import FilterSet

from order.models import Order


class OrderFilter(FilterSet):
    username = CharFilter(field_name="user__username")
    last_name = CharFilter(field_name="user__last_name")

    class Meta:
        model = Order
        fields = ("username", "last_name")