from django.urls import path
from .views import news, news_add, news_details, news_delete
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", news, name="news"),
    path("add/", news_add, name="news_add"),
    path("<int:id>/", news_details, name="news_details"),
    path("<int:id>/delete/", news_delete, name="news_delete"),
]
