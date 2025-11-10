from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.conf import settings
from rest_framework import viewsets
from .models import Product, DeliveryZone, Delivery
from .utils import calcular_ruta, calcular_costo_delivery
from .forms import ProductForm
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.decorators import login_required

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})

def perform_create(self, serializer):
    serializer.save(user=self.request.user)

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})
        
# Editar producto
@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk, seller=request.user)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product-list")
    else:
        form = ProductForm(instance=product)
    return render(request, "products/products_form.html", {"form": form})

# Eliminar producto
@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk, seller=request.user)
    if request.method == "POST":
        product.active = False
        product.save()
        return redirect("product-list")
    return render(request, "products/product_confirm_delete.html", {"product": product})

def crear_delivery(request):
    if request.method == 'POST':
        lat_tienda = -34.6037   # Ejemplo: Buenos Aires
        lng_tienda = -58.3816

        customer_address = request.POST.get('customer_address')
        customer_lat = float(request.POST.get('customer_lat'))
        customer_lng = float(request.POST.get('customer_lng'))

        ruta = calcular_ruta(lat_tienda, lng_tienda, customer_lat, customer_lng)

        if ruta:
            costo = calcular_costo_delivery(
                ruta['distance_km'],
                base_cost=DeliveryZone.objects.first().base_cost if DeliveryZone.objects.exists() else 200,
                cost_per_km=DeliveryZone.objects.first().cost_per_km if DeliveryZone.objects.exists() else 50,
            )

            Delivery.objects.create(
                customer_address=customer_address,
                customer_lat=customer_lat,
                customer_lng=customer_lng,
                distance_km=ruta['distance_km'],
                duration_min=ruta['duration_min'],
                cost=costo,
                geometry=ruta['geometry'],
            )

        return redirect('product_list')

    return render(request, 'products/crear_delivery.html')


def mapa_delivery(request):
    lat_origen, lng_origen = -34.6037, -58.3816  # Obelisco
    lat_destino, lng_destino = -34.6200, -58.4400  # Almagro

    data = calcular_ruta(lat_origen, lng_origen, lat_destino, lng_destino)

    import pprint
    pprint.pprint(data)

    return render(request, "products/mapa_delivery.html", {
        "ruta": data,
        "origen": [lat_origen, lng_origen],
        "destino": [lat_destino, lng_destino],
    })

# lo de MP
# 