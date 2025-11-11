from django.urls import path
from .views import product_list, product_create, product_detail
from . import views

app_name = 'products'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('nuevo/', product_create, name='product_create'),
    path('<int:product_id>/', product_detail, name='product_detail'),
    path("mapa/", views.mapa_delivery, name="mapa_delivery"),
    path('crear_pedido/', views.crear_pedido, name='crear_pedido'),
    path('about/', views.about, name='about'),
    path("api/calcular-delivery/", views.calcular_delivery, name="calcular_delivery"),


]
