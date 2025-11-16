from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseForbidden
from django.conf import settings
from rest_framework import viewsets
from .models import Product, DeliveryZone, Delivery, Category
from .utils import calcular_ruta, calcular_costo_delivery
from .forms import ProductForm
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.decorators import login_required
from django.db.models import Q


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
            return redirect('products:product_list')
    else:
        form = ProductForm()
    return render(request, 'products/products_form.html', {'form': form})

def home(request):
    return render(request, "products/home.html")

def product_list(request):
    category_id = request.GET.get("category")
    query = request.GET.get("q")  
    
    products = Product.objects.filter(active=True)
    categories = Category.objects.all()

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(brand__icontains=query) |
            Q(description__icontains=query)
        )

    if category_id:
        products = products.filter(category_id=category_id)

    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories,
        'selected_category': category_id,
        'query': query,
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk, user=request.user)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("products:product_list")
    else:
        form = ProductForm(instance=product)
    return render(request, "products/products_form.html", {"form": form})

@login_required
def product_delete(request, pk):
    print(">>> LLEGÓ LA VISTA product_delete con método:", request.method)
    product = get_object_or_404(Product, pk=pk, user=request.user)

    if request.method == "POST":
        print(">>> RECIBIDO POST CORRECTAMENTE")
        product.active = False
        product.save()
        return redirect("products:product_list")

    return redirect("products:product_list")



def about(request):
    return render(request, "products/about.html")

def crear_pedido(request):
    if request.method == 'POST':
        lat_tienda = -34.6037
        lng_tienda = -58.3816

        customer_name = request.POST.get('customer_name')
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
                customer_address="",
                customer_lat=customer_lat,
                customer_lng=customer_lng,
                distance_km=ruta['distance_km'],
                duration_min=ruta['duration_min'],
                cost=costo,
                geometry=ruta['geometry'],
            )

        return JsonResponse({
            "success": True,
            "costo": round(float(costo), 2),
            "distancia_km": round(float(ruta['distance_km']), 2),
            "geometry": ruta['geometry'],
        })

def calcular_delivery(request):
    lat_tienda, lng_tienda = -34.6037, -58.3816
    customer_lat = float(request.GET.get("lat"))
    customer_lng = float(request.GET.get("lng"))

    ruta = calcular_ruta(lat_tienda, lng_tienda, customer_lat, customer_lng)

    if ruta:
        costo = calcular_costo_delivery(
            ruta['distance_km'],
            base_cost=DeliveryZone.objects.first().base_cost if DeliveryZone.objects.exists() else 200,
            cost_per_km=DeliveryZone.objects.first().cost_per_km if DeliveryZone.objects.exists() else 50,
        )
        return JsonResponse({
            "success": True,
            "costo": round(float(costo), 2),
            "distancia_km": round(float(ruta['distance_km']), 2),
            "geometry": ruta['geometry'],
        })
    return JsonResponse({"success": False, "error": "No se pudo calcular ruta"})

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
