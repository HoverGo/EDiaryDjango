from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator


class UserManager(BaseUserManager):
    def create_user(self, username, password):
        if username is None:
            raise TypeError("Users must have a username")

        if password is None:
            raise TypeError("Users must have a password")

        user = self.model(username=username)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=50,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z0-9][a-zA-Z0-9_]*$",
                message=("Invalid username"),
                code="invalid_username",
            ),
        ],
    )

    password = models.CharField(
        max_length=25,
        validators=[
            RegexValidator(
                regex=r"^[A-Za-z\d!@#$%^&*()_+]+$",
                message=("Invalid password"),
                code="invalid_password",
            ),
        ],
    )
    num_class = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(11),
        ],
    )
    letter_class = models.CharField(max_length=1, null=True, blank=True)
    profile_img = models.ImageField(blank=True, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "username"

    objects = UserManager()

    def __str__(self):
        return self.username
