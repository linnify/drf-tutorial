from django.db.models.signals import post_save
from django.dispatch import receiver

from order.models import Order


@receiver(post_save, sender=Order, dispatch_uid="notify_post_save_order")
def post_save_order(sender, instance: Order, **kwargs):
    pass