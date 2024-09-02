from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("news/", include("news.urls")),
    path("users/", include("users.urls")),
    path("evaluations/", include("evaluations.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
