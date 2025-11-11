from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Cart, CartItem
from django.contrib import messages
import mercadopago
# from django.conf import settings
from elmercadito import settings
from django.http import JsonResponse

# añadir al carrito
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        item.quantity += 1
        item.save()
    
    messages.success(request, f"✅ '{product.product_name}' se añadió al carrito correctamente.")

    return redirect('products:product_detail', product_id=product.id)


# ver carrito
@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)

    # Total por ítem y total general
    total_general = 0
    for item in items:
        item.subtotal = item.quantity * item.product.price
        total_general += item.subtotal

    context = {
        'cart': cart,
        'items': items,
        'total_general': total_general
    }
    return render(request, 'cart/cart.html', context)

@login_required
def clear_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart.items.all().delete() 
    return redirect('carrito:view_cart')

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    return redirect('carrito:view_cart')

@login_required
def update_quantity(request, item_id, accion):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if accion == "sumar":
        item.quantity += 1
        item.save()
    elif accion == "restar":
        item.quantity -= 1
        if item.quantity <= 0:
            item.delete()
            return redirect("carrito:view_cart")
        item.save()
    return redirect("carrito:view_cart")

@login_required
def create_preference(request):
    """Genera una preferencia de pago para todos los productos del carrito"""
    cart = Cart.objects.filter(user=request.user).first()
    if not cart or not cart.items.exists():
        return JsonResponse({"error": "El carrito está vacío"}, status=400)

    sdk = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_TOKEN)

    items = []
    for item in cart.items.all():
        items.append({
            "title": item.product.product_name,
            "quantity": item.quantity,
            "unit_price": float(item.product.price),
            "currency_id": "ARS",
        })

    preference_data = {
        "items": items,
        "back_urls": {
            "success": request.build_absolute_uri("/pago-exitoso/"),
            "failure": request.build_absolute_uri("/pago-fallido/"),
            "pending": request.build_absolute_uri("/pago-pendiente/"),
        },
        "auto_return": "approved",
    }

    preference = sdk.preference().create(preference_data)
    print("Respuesta MercadoPago:", preference)  # <- Te muestra el detalle en consola

    if preference.get("status") != 201:
        return JsonResponse({
            "error": "No se pudo crear la preferencia",
            "detalle": preference
        }, status=400)

    return JsonResponse({"init_point": preference["response"]["init_point"]})