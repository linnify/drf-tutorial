import factory

from order.models import Order
from store.tests.factories import StoreFactory
from users.tests.factories import UserFactory


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    user = factory.SubFactory(UserFactory)
    store = factory.SubFactory(StoreFactory)