from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from store.models import Store, Address, Stock
from store.serializers import StoreSerializer, AddressSerializer, StockSerializer


class StoresViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class AddressesViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class StocksViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("product__name",)
    ordering = ("id")
    ordering_fields = ("product__name",)