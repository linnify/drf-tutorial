from django.db import models
from django.db.models import F, Sum

from common.decorators import profile


class RawOrderManager(models.Manager):

    def raw_orders(self):
        return self.raw(
            "SELECT * from order_order"
        )

    def raw_order_id(self, id):
        return self.raw(
            f"SELECT * from order_order WHERE id={id} LIMIT 1"
        )[0]


class OrderManager(models.Manager):

    @profile
    def example_select_related_bad(self):
        orders = self.all()
        print("Example without select related")
        for order in orders:
            print("UserId", order.user.id)

    @profile
    def example_select_related_ok(self):
        orders = self.all().select_related("user")
        print("Example with select related")
        for order in orders:
            print("UserId", order.user.id)

    @profile
    def example_f_function(self):
        self.update(paid_amount=F("paid_amount") + 10)

    @profile
    def example_total_amount_paid(self):
        total_paid_amount =  self.all().aggregate(total_paid_amount=Sum("paid_amount"))
        print("Total paid Amount", total_paid_amount)

    @profile
    def example_count_bad(self):
        print("Count with len", len(self.all()))

    @profile
    def example_count_ok(self):
        print("Count", self.count())

    @profile
    def example_values_list(self):
        print("Value List Flat True User Ids", self.all().values_list("user__id", flat=True))

    @profile
    def example_values(self):
        print("Values", self.all().values("user", "id", "paid_amount"))
