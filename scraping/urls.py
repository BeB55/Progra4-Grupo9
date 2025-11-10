from django.urls import path
from . import views

app_name = "scraping"
from .views import CompararPrecios

urlpatterns = [
    path('comparar/<str:nombre>/', CompararPrecios.as_view(), name='comparar'),
]
