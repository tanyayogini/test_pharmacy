import pytest
from django.core.exceptions import ValidationError

from products.validators import validate_ean13


def test_ean13_validator():
    assert validate_ean13('1111111111116') == None
    with pytest.raises(ValidationError):
        validate_ean13('1111111111111')
    with pytest.raises(ValidationError):
        validate_ean13('qwe')