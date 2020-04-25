from rest_framework import viewsets

from brand.models import Product, Brand
from brand.serializers import BrandSerializer, ProductSerializer


class BrandsViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

