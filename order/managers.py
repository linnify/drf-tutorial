from django.db import models


class OrderManager(models.Manager):

    def raw_orders(self):
        return self.raw(
            "SELECT * from order_order"
        )

    def raw_order_id(self, id):
        return self.raw(
            f"SELECT * from order_order WHERE id={id} LIMIT 1"
        )[0]