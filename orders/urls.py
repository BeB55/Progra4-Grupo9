from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("mis-compras/", views.mis_compras, name="mis_compras"),
    path("delete-order/<int:order_id>/", views.delete_order, name="delete_order"),
]
