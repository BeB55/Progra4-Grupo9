from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderItem

@receiver([post_save, post_delete], sender=OrderItem)
def actualizar_total_orden(sender, instance, **kwargs):
    order = instance.order
    order.total = order.calculate_total()
    order.save(update_fields=["total"])
