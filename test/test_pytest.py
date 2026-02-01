import pytest
from src.calculator import fun1, fun2, fun3, fun4, fun5


@pytest.mark.parametrize(
    "x,y,expected",
    [(1, 2, 3), (0, 0, 0), (-1, 1, 0), (2.5, 0.5, 3.0)]
)
def test_fun1_param(x, y, expected):
    assert fun1(x, y) == expected



def test_fun1():
    assert fun1(2, 3) == 5


def test_fun2():
    assert fun2(10, 4) == 6


def test_fun3():
    assert fun3(3, 5) == 15


def test_fun5_division():
    assert fun5(10, 2) == 5


def test_fun5_divide_by_zero():
    with pytest.raises(ValueError):
        fun5(10, 0)



def test_fun4():
    assert fun4(2, 3) == (2 + 3) + (2 - 3) + (2 * 3)
