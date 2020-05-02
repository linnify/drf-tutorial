from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from order import views

router = DefaultRouter(trailing_slash=False)
router.register("orders", views.OrdersViewSet, basename="orders")

orders_router = NestedDefaultRouter(
    router, r"orders", lookup="order"
)
orders_router.register(
    r"items", views.OrderItemsModelViewSet, basename="items"
)

urlpatterns = [
    url(r"^", include(router.urls)),
    url(r"^", include(orders_router.urls)),
]