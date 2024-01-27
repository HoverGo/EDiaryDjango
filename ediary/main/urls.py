from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="main"),
    path("news/", views.news, name="news"),
    path("about/", views.about, name="about"),
    path("schedule/", views.schedule, name="schedule"),
]
