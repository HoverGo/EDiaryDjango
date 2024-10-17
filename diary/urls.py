from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import diary, diary_add
from django.urls import path, include

urlpatterns = [
    path("", diary, name="diary"),
    path("add/", diary_add, name="diary_add")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
