from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    AdminTestView,
    CustomerTestView,
    InventoryManagerTestView,
    RegisterView,
)


urlpatterns = [
    path(
        "register/",
        RegisterView.as_view(),
        name="register",
    ),
    path(
        "login/",
        TokenObtainPairView.as_view(),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(),
        name="token-refresh",
    ),
    path(
        "admin-test/",
        AdminTestView.as_view(),
        name="admin-test",
    ),
    path(
    "manager-test/",
    InventoryManagerTestView.as_view(),
    name="manager-test",
    ),
    path(
    "customer-test/",
    CustomerTestView.as_view(),
    name="customer-test",
    ),
]