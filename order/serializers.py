from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.utils.translation import gettext as _
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, Serializer, ReadOnlyField,\
    DateTimeField, FloatField, CharField, IntegerField

from order.models import Order, OrderItem
from store.serializers import StoreSerializer


class CreateOrderSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = ("id", "store", "user")


class ReadOnlyOrderSerializer(Serializer):
    id = IntegerField()
    store = StoreSerializer()
    user = ReadOnlyField(source="user_id")
    date = DateTimeField()
    paid_amount = FloatField()
    status = CharField()


class OrderItemSerializer(ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ("id", "order", "product", "quantity", "total_price", "lock_price")
        read_only_fields = ("total_price", "lock_price")

    def validate(self, attrs):
        attrs = super().validate(attrs)
        store = attrs.get("order").store
        product = attrs.get("product")

        self.__validate_stock(store, product, attrs.get("quantity"))
        self.__validate_store(store, product)
        return attrs

    def __validate_stock(self, store, product_id, quantity):
        try:
            stock = store.stocks.get(product_id=product_id).only("quantity")
            if quantity > stock.quantity:
                raise ValidationError({
                    "quantity": _(f"The quantity can not be greater"
                                  f" than {stock.quantity}")
                })

        except ObjectDoesNotExist:
            raise ValidationError({
                "product": _("The product is not in stock")
            })
        except MultipleObjectsReturned:
            raise ValidationError({
                "product": _("Multiple products are in stock")
            })

    def __validate_store(self, store, product):
        try:
            if store.brand_id != product.brand_id:
                raise ValidationError({
                    "product": _("The store brand and the product brand are"
                                 " not the same")
                })
        except AttributeError:
            raise ValidationError({
                "product": _("Check if the product or the store have brands.")
            })


class UpdateOrderItemSerializer(ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ("id", "quantity",)
        read_only_fields = ("total_price", "lock_price", "product", "order")