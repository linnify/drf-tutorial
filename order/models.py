from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext as _
from brand.models import Product
from order.managers import RawOrderManager, OrderManager
from store.models import Store


class Order(models.Model):
    CANCELED = "canceled"
    IN_PROGRESS = "in-progress"
    COMPLETED = "completed"
    STATUS = (
        (CANCELED, _("Canceled")),
        (IN_PROGRESS, _("In Progress")),
        (COMPLETED, _("Completed"))
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    store = models.ForeignKey(Store, on_delete=models.PROTECT, related_name="orders")
    status = models.CharField(choices=STATUS, max_length=255, default=IN_PROGRESS)
    paid_amount = models.FloatField(validators=[MinValueValidator(0)], default=0)
    date = models.DateTimeField(auto_now_add=True)
    objects = OrderManager()
    raw_objects = RawOrderManager()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="order_items"
    )
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    lock_price = models.FloatField(
        validators=[MinValueValidator(0)],
        default=0,
        help_text="The price that was set on the product when the item was put in the "
                  "order.")

    def save(self, *args, **kwargs):
        if self.id is None:
            self.lock_price = self.product.price
        super().save(*args, **kwargs)

    @property
    def total_price(self):
        return self.lock_price * self.quantity