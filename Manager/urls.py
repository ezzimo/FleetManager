from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("account.urls", namespace="account")),
    path("refuel/", include("refuel.urls", namespace="refuel")),
    path("", include("vehicle.urls", namespace="vehicle")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
