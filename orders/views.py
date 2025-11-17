from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Order

@login_required
def mis_compras(request):
    estado = request.GET.get("estado")  # lee el filtro desde la URL
    orders = Order.objects.filter(user=request.user)
    if estado:
        orders = orders.filter(status=estado)
    orders = orders.order_by("-created_at")
    return render(request, "orders/mis_compras.html", {"orders": orders})

@login_required
def delete_order(request, order_id):
    # Busca la orden del usuario actual
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order.delete()
    # Redirige de nuevo a la lista de compras
    return redirect("orders:mis_compras")