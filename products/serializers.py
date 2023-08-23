from rest_framework import serializers

from products.models import ProductClient


class ProductClientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ProductClient
