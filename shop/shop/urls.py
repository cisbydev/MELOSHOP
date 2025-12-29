from .import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page_one/', include('app_shop.urls')),
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
