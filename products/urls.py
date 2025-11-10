from django.urls import path
from .views import product_list, product_create, product_detail

app_name = 'products'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('nuevo/', product_create, name='product_create'),
    path('<int:product_id>/', product_detail, name='product_detail'),
]
