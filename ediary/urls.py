from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import active_users

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("news/", include("news.urls")),
    path("users/", include("users.urls")),
    path("diary/", include("diary.urls")),
    path('active-users/', active_users, name='active_users'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
