# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model for the inventory management system.
    """

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        INVENTORY_MANAGER = "INVENTORY_MANAGER", "Inventory Manager"
        CUSTOMER = "CUSTOMER", "Customer"

    email = models.EmailField(
        unique=True,
    )

    first_name = models.CharField(
        max_length=100,
    )

    last_name = models.CharField(
        max_length=100,
        blank=True,
    )

    role = models.CharField(
        max_length=30,
        choices=Role.choices,
        default=Role.CUSTOMER,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = [
        "first_name",
    ]

    def __str__(self):
        return self.email