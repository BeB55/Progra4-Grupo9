from django.db import models
from django.conf import settings
from products.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pendiente"),
        ("paid", "Pagada"),
        ("shipped", "Enviada"),
        ("delivered", "Entregada"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        order_id = str(self.id) if self.id is not None else "sin ID"
        user_name = str(self.user) if self.user is not None else "Usuario sin asignar"
        total = f"${self.total:.2f}" if self.total is not None else "$0.00"
        status = str(self.get_status_display()) if self.status else "Sin estado"
        return f"Orden {order_id} - {user_name} - Total {total} - Estado: {status}"

    def calculate_total(self):
        return sum(item.subtotal() for item in self.items.all())

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.total = self.calculate_total()
        super().save(update_fields=["total"])


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def subtotal(self):
        return self.quantity * self.price

    def save(self, *args, **kwargs):
        if self.price is None:
            self.price = self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        order_id = str(self.order.id) if self.order and self.order.id else "sin ID"
        product_name = self.product.name if self.product else "Producto sin asignar"
        quantity = self.quantity if self.quantity else 0
        subtotal = f"${self.subtotal():.2f}" if self.price is not None else "$0.00"
        return f"Orden {order_id} - {product_name} x{quantity} ({subtotal})"
