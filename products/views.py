from rest_framework.viewsets import ModelViewSet

from products.models import ProductClient
from products.serializers import ProductClientSerializer


# Create your views here.
class ProductClientViewSet(ModelViewSet):
    queryset = ProductClient.objects.all()
    serializer_class = ProductClientSerializer
