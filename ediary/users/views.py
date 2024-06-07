from django.shortcuts import render, redirect
from .services.services import login, logout
from .forms import UserLoginForm
from django.contrib.auth.decorators import login_required


def users_login(request):
    data = {}
    form = UserLoginForm()

    if request.method == "POST":
        if login(request):
            return redirect("main")
        else:
            data["form_error"] = "Invalid data"


    data["form"] = form
    return render(request, "users/users_login.html", data)

@login_required
def users_logout(request):
    if request.user:
        logout(request)
    return redirect("main")

def users_registration(request):
    data = {}
    return render(request, "users/users_registration.html", data)
