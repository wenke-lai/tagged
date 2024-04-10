from __future__ import annotations

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models


class Manager(UserManager):

    def _create_user(
        self, email: str, password: str | None, **extra_fields: dict
    ) -> User:
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save()
        return user

    def create_superuser(
        self, email: str | None, password: str | None, **extra_fields: dict
    ) -> User:
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self._create_user(email, password, **extra_fields)

    def create_user(
        self, email: str, password: str | None, **extra_fields: dict
    ) -> User:
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)

        return self._create_user(email, password, **extra_fields)


class UserPermissionsMixin(PermissionsMixin):
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


class User(AbstractBaseUser, UserPermissionsMixin):
    # main fields
    user_id = models.BigAutoField(primary_key=True)

    username = models.CharField(max_length=255, **settings.NULLABLE)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    # additional fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    objects = Manager()

    def __str__(self) -> str:
        return self.username or self.email.split("@", maxsplit=1)[0]
