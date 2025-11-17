from django.contrib import admin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "brand", "price", "active", "created", "updated")   # columnas que ves en la lista
    search_fields = ("name", "description", "brand", "user__username")                  # campos por los que podés buscar
    list_filter = ("active", "category", "user", "created")                             # filtros en la barra lateral
    ordering = ("-created",)                                                            # orden por fecha de creación

def get_readonly_fields(self, request, obj=None):
        # Si el producto existe y el usuario no es el autor, no puede cambiar 'active'
        if obj and obj.user != request.user:
            return self.readonly_fields + ("active",)
        return self.readonly_fields

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
