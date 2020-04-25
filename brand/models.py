from django.core.validators import MinValueValidator
from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="products")
    price = models.FloatField(validators=[MinValueValidator(0)])
    name = models.CharField(max_length=255)
