from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import diary
from django.urls import path, include

urlpatterns = [
    path("", diary, name="diary"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
