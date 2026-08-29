from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsAdmin, IsInventoryManager

from .models import Product
from .serializers import ProductSerializer


class InventoryTestView(APIView):
    """
    Test endpoint for inventory access.

    Accessible only to ADMIN and INVENTORY_MANAGER users.
    """

    permission_classes = [
        IsAuthenticated,
        IsAdmin | IsInventoryManager,
    ]

    def get(self, request):
        return Response(
            {
                "message": "Inventory API access granted.",
                "email": request.user.email,
                "role": request.user.role,
            }
        )


class ProductViewSet(viewsets.ModelViewSet):
    """
    CRUD API for products.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdmin | IsInventoryManager,
    ]