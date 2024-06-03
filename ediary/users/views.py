from django.shortcuts import render
from .services.services import login


def users_login(request):
    data = {}
    return render(request, "users/users_login.html", data)
