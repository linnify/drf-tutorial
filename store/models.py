from django.db import models

from brand.models import Brand, Product


class Address(models.Model):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    street_no = models.PositiveIntegerField()
    country = models.CharField(max_length=255)


class Store(models.Model):
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True, blank=True, related_name="store")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="stores")
    name = models.CharField(max_length=100)


class Stock(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="stocks")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="stocks")
    quantity = models.PositiveIntegerField()