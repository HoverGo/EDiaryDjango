from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import diary, diary_add, diary_record, delete_diary_record
from django.urls import path, include

urlpatterns = [
    path("", diary, name="diary"),
    path("<int:id>/", diary_record, name="diary_record"),
    path("<int:id>/delete/", delete_diary_record, name="delete_diary_record"),
    path("add/", diary_add, name="diary_add"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
