from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('nuevo/', views.product_create, name='product_create'),
    path('editar/<int:pk>/', views.product_edit, name='product_edit'),
    path('eliminar/<int:pk>/', views.product_delete, name='product_delete'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path("mapa/", views.mapa_delivery, name="mapa_delivery"),
    path('crear_pedido/', views.crear_pedido, name='crear_pedido'),
    path('about/', views.about, name='about'),
    path("mis-productos/", views.mis_productos, name="mis_productos"),
    path("api/calcular-delivery/", views.calcular_delivery, name="calcular_delivery"),
]
