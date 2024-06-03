from django.urls import path
from .views import users_login
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("login/", users_login, name="login"),
]
