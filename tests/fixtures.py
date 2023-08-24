import pytest

from products.models import Product, ProductClient


@pytest.mark.django_db
@pytest.fixture
def get_product():
    product = Product.objects.create(ean13='1111111111116', name_prep='test')
    return product

@pytest.mark.django_db
@pytest.fixture
def get_product_client(get_product):
    product_client = ProductClient.objects.create(ean13=get_product, name_prep='test_client')

    return product_client