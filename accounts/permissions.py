from rest_framework.permissions import BasePermission

from .models import User


class IsAdmin(BasePermission):
    """
    Allows access only to users with ADMIN role.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == User.Role.ADMIN
        )


class IsInventoryManager(BasePermission):
    """
    Allows access only to users with INVENTORY_MANAGER role.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == User.Role.INVENTORY_MANAGER
        )


class IsCustomer(BasePermission):
    """
    Allows access only to users with CUSTOMER role.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == User.Role.CUSTOMER
        )