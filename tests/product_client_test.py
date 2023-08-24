import pytest
from rest_framework import status


@pytest.mark.django_db
def test_get_product_client_list(client, get_product_client):
    response = client.get("/products/client/")
    expected_response = [
        {
            "id": 1,
            "name_prep": "test_client",
            "ean13": "1111111111116"
        }]
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response
