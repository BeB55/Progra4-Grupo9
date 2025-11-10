from django.db import models
from django.conf import settings
from decimal import Decimal

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100, default='sin nombre')
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to='products/%Y/%m/%d/',
        blank=True,
        null=True
    )
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
    
class DeliveryZone(models.Model):
    name = models.CharField(max_length=100)
    max_distance_km = models.FloatField(default=10)
    base_cost = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('200.00'))
    cost_per_km = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('50.00'))

    def __str__(self):
        return self.name


class Delivery(models.Model):
    order_id = models.IntegerField(null=True, blank=True)
    customer_address = models.CharField(max_length=255)
    customer_lat = models.FloatField()
    customer_lng = models.FloatField()
    distance_km = models.FloatField(null=True, blank=True)
    duration_min = models.FloatField(null=True, blank=True)
    cost = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    geometry = models.JSONField(null=True, blank=True)
    status = models.CharField(max_length=20, default='pending')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Delivery #{self.pk} (status: {self.status})"

