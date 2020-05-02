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


class UpdateOrderItemSerializer(ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ("id", "quantity",)
        read_only_fields = ("total_price", "lock_price", "product", "order")