from django.contrib import admin
from django.urls import path, include
from users.views import home_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('productos/', include(('products.urls', 'products'), namespace='products')),
    path('carrito/', include('cart.urls')),
    path('scraping/', include('scraping.urls')),
    path("orders/", include("orders.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)