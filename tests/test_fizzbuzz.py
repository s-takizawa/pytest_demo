import pytest
from src.fizzbuzz import FizzBuzz


# Preprocessing
@pytest.fixture(scope='function', autouse=True)
def fizzbuzz():
    return FizzBuzz()


def test_1を渡したら文字列1を返す(fizzbuzz):
    assert type(fizzbuzz.convert(1)) is str
    assert fizzbuzz.convert(1) == '1'


def test_2を渡したら文字列2を返す(fizzbuzz):
    assert fizzbuzz.convert(2) == '2'


def test_3を渡したら文字列Fizzを返す(fizzbuzz):
    assert fizzbuzz.convert(3) == 'Fizz'


def test_5を渡したら文字列Buzzを返す(fizzbuzz):
    assert fizzbuzz.convert(5) == 'Buzz'


def test_15を渡したら文字列FizzBuzzを返す(fizzbuzz):
    assert fizzbuzz.convert(15) == 'FizzBuzz'


def test_文字列aを渡したらTypeErrorが発生(fizzbuzz):
    with pytest.raises(TypeError):
        fizzbuzz.convert('a')
