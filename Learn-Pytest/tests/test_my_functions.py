import pytest
import src.my_functions as my_functions


def test_add():
    result = my_functions.add(a=5, b=10)
    assert result == 15


def test_add_string():
    result = my_functions.add(a="I like ", b="burgers")
    assert result == "I like burgers"


def test_divide():
    result = my_functions.divide(a=10, b=10)
    assert result == 1


def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(a=20, b=0)
        assert True
