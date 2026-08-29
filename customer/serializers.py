from rest_framework import serializers

from inventory.models import Product


class CustomerProductSerializer(serializers.ModelSerializer):
    """
    Serializer for products visible to customers.
    """

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "sku",
            "description",
            "price",
        ]