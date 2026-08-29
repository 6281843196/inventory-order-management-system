from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsCustomer
from inventory.models import Product

from .serializers import CustomerProductSerializer


class CustomerProductListView(ListAPIView):
    """
    Allows customers to view active products.
    """

    serializer_class = CustomerProductSerializer

    permission_classes = [
        IsAuthenticated,
        IsCustomer,
    ]

    def get_queryset(self):
        return Product.objects.filter(
            is_active=True
        )