from django.contrib import admin
from django.urls import path, include
from users.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('api/auth/', include('rest_framework.urls')),
    path('', home_view, name='home'),
    path('productos/', include('products.urls')),

]
