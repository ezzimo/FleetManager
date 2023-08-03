from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path
from django.views.generic import TemplateView

from .settings.api import router

urlpatterns = [
    path("", include("vehicle.urls", namespace="vehicle")),
    path("account/", include("account.urls", namespace="account")),
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("company_management/", include("CompanyManagement.urls", namespace="company_management")),
    path("inventory/", include("inventory.urls", namespace="inventory")),
    path("maintenance/", include("maintenance.urls", namespace="maintenance")),
    path("refuel/", include("refuel.urls", namespace="refuel")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
