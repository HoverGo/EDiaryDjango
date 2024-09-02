import re
from ..models import User
from django.contrib.auth import login, logout, authenticate
from ..forms import UserLoginForm, UserRegistrationForm


def account_login(request) -> bool:  
    form = UserLoginForm(data=request.POST)
    if form.is_valid():
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return True
    return False

def account_logout(request) -> None:
    logout(request)
    return None

def account_registration(request) -> bool:
    form = UserRegistrationForm(data=request.POST)
    password_pattern = r"^[A-Za-z\d!@#$%^&*()_+]+$"
    if form.is_valid():
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        # Пароль должен соответствовать заданному паттерну, иметь количество символов не менее 8, и совпадать со 2 введённым паролем
        if (re.match(password_pattern, password1)) and (len(password1) >= 8) and (password1 == password2):
            user = User.objects.create_user(email=email, password=password1)

            # Автоматический логин при успешной регистрации пользователя
            login(request, user)
            return True
    return False