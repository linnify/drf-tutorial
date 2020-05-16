from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, \
    DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from order.filters import OrderFilter
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
    filter_backends = (DjangoFilterBackend,)
    filterset_class = OrderFilter
    filter_fields = ("status",)

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
    permission_classes = (IsOwnerUser, IsAuthenticated)

    def get_queryset(self):
        order = get_object_or_404(Order.objects.all(), id=self.kwargs.get("order_pk"))
        self.check_object_permissions(self.request, order)

        return order.items.all()

    def get_object(self):
        return get_object_or_404(self.get_queryset(), id=self.kwargs.get("pk"))

    def get_serializer_class(self):
        if self.action in ["update", "partial_update"]:
            return UpdateOrderItemSerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        request.data["order"] = kwargs.get("order_pk")
        return super().create(request, *args, **kwargs)


@api_view(["GET"])
def raw_order(request):
    orders = Order.raw_objects.raw_orders()
    serializer = ReadOnlyOrderSerializer(instance=orders, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
def raw_order_id(request, pk):
    order = Order.raw_objects.raw_order_id(pk)
    serializer = ReadOnlyOrderSerializer(instance=order)
    return Response(data=serializer.data)