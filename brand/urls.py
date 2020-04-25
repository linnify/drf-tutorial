from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from brand import views

router = routers.DefaultRouter(trailing_slash=False)
router.register("products", views.ProductsViewSet)
router.register("brands", views.BrandsViewSet)


urlpatterns = [url(r"^", include(router.urls))]