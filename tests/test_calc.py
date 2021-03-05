import pytest
from src.calc import Calc


# Preprocessing
@pytest.fixture(scope='function', autouse=True)
def cl():
    return Calc()


def test_constructor():
    cl1 = Calc()
    assert cl1.x == 0
    assert cl1.y == 0
    cl2 = Calc(1)
    assert cl2.x == 1
    assert cl2.y == 0
    cl3 = Calc(2, 3)
    assert cl3.x == 2
    assert cl3.y == 3


def test_add(cl):
    assert cl.add(1, 2) == 3


def test_minus(cl):
    assert cl.minus(5, 3) == 2
    assert cl.minus(1, 2) == -1, '引き算：マイナス値'


def test_multiply(cl):
    assert cl.multiply(2, 3) == 6
    assert cl.multiply(3, 0) == 0


def test_divide(cl):
    assert cl.divide(4, 2) == 2
    assert cl.divide(5, 3) == 1
    with pytest.raises(ZeroDivisionError):
        cl.divide(2, 0)
