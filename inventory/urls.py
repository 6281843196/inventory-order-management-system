from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import InventoryTestView, ProductViewSet


router = DefaultRouter()

router.register(
    "products",
    ProductViewSet,
    basename="product",
)


urlpatterns = [
    path(
        "",
        InventoryTestView.as_view(),
        name="inventory-test",
    ),
    path(
        "",
        include(router.urls),
    ),
]