from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import (
    IsAdmin,
    IsCustomer,
    IsInventoryManager,
)
from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    """
    API endpoint for user registration.
    """

    serializer_class = RegisterSerializer


class AdminTestView(APIView):
    """
    Test endpoint accessible only to ADMIN users.
    """

    permission_classes = [IsAdmin]

    def get(self, request):
        return Response(
            {
                "message": "Welcome Admin!",
                "email": request.user.email,
                "role": request.user.role,
            }
        )

class InventoryManagerTestView(APIView):
    """
    Test endpoint accessible only to INVENTORY_MANAGER users.
    """

    permission_classes = [IsInventoryManager]

    def get(self, request):
        return Response(
            {
                "message": "Welcome Inventory Manager!",
                "email": request.user.email,
                "role": request.user.role,
            }
        )
class CustomerTestView(APIView):
    """
    Test endpoint accessible only to CUSTOMER users.
    """

    permission_classes = [IsCustomer]

    def get(self, request):
        return Response(
            {
                "message": "Welcome Customer!",
                "email": request.user.email,
                "role": request.user.role,
            }
        )