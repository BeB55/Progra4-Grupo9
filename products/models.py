from django.db import models
from django.conf import settings
from decimal import Decimal

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name


from django.conf import settings
from django.db import models

class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField("Nombre del producto", max_length=200, default="sin nombre")
    brand = models.CharField("Marca", max_length=100, blank=True, null=True)
    description = models.TextField("Descripción", blank=True)
    price = models.DecimalField("Precio", max_digits=10, decimal_places=2, default=0)
    stock = models.PositiveIntegerField("Stock disponible", default=0)  # ✅ solo una vez
    image = models.ImageField("Agregar imagen", upload_to="products/%Y/%m/%d/", blank=True, null=True)
    category = models.ForeignKey(
        "products.Category",
        verbose_name="Categoría",
        on_delete=models.CASCADE,
        related_name="products",
        null=True, blank=True
    )
    active = models.BooleanField("Activo", default=True)  # ✅ control de visibilidad
    created = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField("Última actualización", auto_now=True)

    def save(self, *args, **kwargs):
        if not self.category:
            from products.models import Category
            general, _ = Category.objects.get_or_create(
                name="General",
                defaults={"description": "Categoría por defecto"}
            )
            self.category = general
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.brand or 'sin marca'})"


    
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

class Comment(models.Model):
    product = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField("Comentario")
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Comentario de {self.user.username} en {self.product.name}"
