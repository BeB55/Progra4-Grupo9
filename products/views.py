from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Product
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
        form = ProductForm(request.POST)
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
        