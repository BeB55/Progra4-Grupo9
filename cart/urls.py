from django.urls import path
from . import views

app_name = 'carrito'

urlpatterns = [
    # Carrito
    path('', views.view_cart, name='view_cart'),
    path('añadir_al_carrito/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path("eliminar/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("vaciar/", views.clear_cart, name="clear_cart"), 
    path("actualizar/<int:item_id>/<str:accion>/", views.update_quantity, name="update_quantity"), 
    
    # Pagos
    path("pago/", views.create_preference, name="crear-preferencia"),
    path("pago/exitoso/", views.pago_exitoso, name="pago_exitoso"),
    path("pago/fallido/", views.pago_fallido, name="pago_fallido"),
    path("pago/pendiente/", views.pago_pendiente, name="pago_pendiente"),
]
