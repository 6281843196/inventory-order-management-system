from django.urls import path

from .views import CustomerProductListView


urlpatterns = [
    path(
        "products/",
        CustomerProductListView.as_view(),
        name="customer-products",
    ),
]