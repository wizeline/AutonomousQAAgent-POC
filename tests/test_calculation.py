import pytest
from calculation import get_square_root, is_positive_number

def test_get_square_root_positive_number():
    assert get_square_root(16) == 4.0
    assert get_square_root(2) == pytest.approx(1.4142135623730951)
    assert get_square_root(0) == 0.0

def test_get_square_root_negative_number():
    with pytest.raises(ValueError):
        get_square_root(-1)

def test_is_positive_number():
    assert is_positive_number(1) == True
    assert is_positive_number(0.5) == True
    assert is_positive_number(0) == False
    assert is_positive_number(-1) == False
    assert is_positive_number(-0.5) == False