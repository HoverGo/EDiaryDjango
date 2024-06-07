from ..models import *
from django.contrib import auth
from ..forms import UserLoginForm

def login(request) -> bool:  
    form = UserLoginForm(data=request.POST)
    if form.is_valid():
        email = request.POST["email"]
        password = request.POST["password"]
        user = auth.authenticate(email=email, password=password)
        if user:
            print(456)  
            auth.login(request, user)
            return True
    return False

def logout(request) -> None:
    auth.logout(request)
    return None