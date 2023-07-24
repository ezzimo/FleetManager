from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path
from django.views.generic import TemplateView

from .settings.api import router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("account/", include("account.urls", namespace="account")),
    path("refuel/", include("refuel.urls", namespace="refuel")),
    path("maintenance/", include("maintenance.urls", namespace="maintenance")),
    path("", include("vehicle.urls", namespace="vehicle")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
