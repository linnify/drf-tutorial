from rest_framework import serializers

from store.models import Store, Address, Stock


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ("id", "country", "city", "street", "street_no")


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ("id", "name", "address", "brand")


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = ("id", "store", "product", "quantity")

