from rest_framework import serializers

from brand.models import Product, Brand


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ("id", "name", "description")


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("id", "brand", "name", "price")