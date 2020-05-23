import factory

from brand.tests.factories import BrandFactory
from store.models import Store, Address


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address

    city = "Cluj-Napoca"
    street = "Macinului"
    street_no = "34"
    country = "Romania"


class StoreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Store

    name = "Nike Iulius"
    brand = factory.SubFactory(BrandFactory)
    address = factory.SubFactory(AddressFactory)