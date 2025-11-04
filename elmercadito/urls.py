from django.contrib import admin
from django.urls import path, include
from users.views import home_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    # path('auth/', include('users.urls')),
    path('api/auth/', include('rest_framework.urls')),
    path('', home_view, name='home'),
    path('productos/', include('products.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)