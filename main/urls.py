from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Info pages
    path("", index, name="main"),
    path("about/", about, name="about"),
    path("schedule/", schedule, name="schedule"),
]
