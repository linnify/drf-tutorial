from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from store import views

router = routers.DefaultRouter(trailing_slash=False)
router.register("stores", views.StoresViewSet)
router.register("addresses", views.AddressesViewSet)
router.register("stocks", views.StocksViewSet)


urlpatterns = [url(r"^", include(router.urls))]