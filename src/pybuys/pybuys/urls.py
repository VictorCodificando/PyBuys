from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.views.static import serve

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", include("core.urls")),
        path("product/", include("product.urls")),
        path("buysSales/", include("buysSales.urls")),
        path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),  # Sirve archivos de medios
        path('static/<path:path>', serve, {'document_root': settings.STATIC_ROOT}),  # Sirve archivos estáticos
    ]
)
