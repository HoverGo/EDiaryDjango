from django.shortcuts import render, redirect
from .services.services import account_login, account_logout, account_registration
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required


def users_login(request):
    data = {}
    form = UserLoginForm()

    if request.method == "POST":
        if account_login(request):
            return redirect("main")
        else:
            data["form_error"] = "Invalid data"


    data["form"] = form
    return render(request, "users/users_login.html", data)

@login_required
def users_logout(request):
    if request.user:
        account_logout(request)
    return redirect("main")

def users_registration(request):
    data = {}
    form = UserRegistrationForm()

    if request.method == "POST":
        if account_registration(request):
            return redirect("main")
        else:
            data["form_error"] = "Invalid data"

    data["form"] = form 
    return render(request, "users/users_registration.html", data)
