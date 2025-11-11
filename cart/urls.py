from django.urls import path
from . import views

app_name = 'carrito'

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('añadir_al_carrito/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path("eliminar/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("vaciar/", views.clear_cart, name="clear_cart"), 
    path("actualizar/<int:item_id>/<str:accion>/", views.update_quantity, name="update_quantity"), 
]
