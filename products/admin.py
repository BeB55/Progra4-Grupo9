from django.contrib import admin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "brand", "price", "active", "created", "updated")   # columnas que ves en la lista
    search_fields = ("name", "description", "brand", "user__username")                  # campos por los que podés buscar
    list_filter = ("active", "category", "user", "created")                             # filtros en la barra lateral
    ordering = ("-created",)                                                            # orden por fecha de creación

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
