from django.urls import path
from .views import add_to_cart, view_cart

app_name = 'carrito'

urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('añadir_al_carrito/<int:product_id>/', add_to_cart, name='add_to_cart'),
]
