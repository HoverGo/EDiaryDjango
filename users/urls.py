from django.urls import path
from .views import users_login, users_logout , users_registration
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("login/", users_login, name="login"),
    path("logout/", users_logout, name="logout"),
    path("registration/", users_registration, name="registration"),
]
