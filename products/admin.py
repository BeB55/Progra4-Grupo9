from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "user", "brand", "price", "active", "created_at")   # columnas que ves en la lista
    search_fields = ("product_name", "description", "brand", "user__username")          # campos por los que podés buscar
    list_filter = ("active", "created_at", "user")                               # filtros en la barra lateral