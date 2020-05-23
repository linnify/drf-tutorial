from django.test import TestCase

from common.decorators import profile
from order.models import Order
from order.tests.factories import OrderFactory
from store.tests.factories import StoreFactory
from users.tests.factories import UserFactory


class TestOrderManager(TestCase):

    @classmethod
    def setUpTestData(cls):
        OrderFactory.create_batch(100)

    def test_select_related(self):
        Order.objects.example_select_related_ok()

    def test_aggregate(self):
        Order.objects.example_total_amount_paid()

    def test_count(self):
        Order.objects.example_count_ok()

    def test_values(self):
        Order.objects.example_values()

    def test_values_list(self):
        Order.objects.example_values_list()

    def test_f_function(self):
        Order.objects.example_f_function()
        order = OrderFactory()
        order.paid_amount = 10
        order.save()

    @profile
    def test_bulk_create(self):
        len(Order.objects.all().defer("user"))
