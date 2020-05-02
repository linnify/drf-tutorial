from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, \
    DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from order.models import Order, OrderItem
from order.serializers import ReadOnlyOrderSerializer, CreateOrderSerializer, \
    OrderItemSerializer, UpdateOrderItemSerializer
from tutorial.permissions import IsOwnerUser


class OrdersViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    serializer_class = ReadOnlyOrderSerializer
    permission_classes = (IsAuthenticated, IsOwnerUser)
    queryset = Order.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_object(self):
        instance = get_object_or_404(self.queryset, id=self.kwargs.get("pk"))
        self.check_object_permissions(self.request, instance)
        return instance

    def get_serializer_class(self):
        if self.action == "create":
            return CreateOrderSerializer

        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        return super().create(request, *args, **kwargs)


class OrderItemsModelViewSet(ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()

    def get_queryset(self):
        return OrderItem.objects.filter(
            order__user=self.request.user,
            order_id=self.kwargs.get("order_pk")
        )

    def get_object(self):
        return get_object_or_404(self.get_queryset(), id=self.kwargs.get("pk"))

    def get_serializer_class(self):
        if self.action in ["update", "partial_update"]:
            return UpdateOrderItemSerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        request.data["order"] = kwargs.get("order_pk")
        return super().create(request, *args, **kwargs)