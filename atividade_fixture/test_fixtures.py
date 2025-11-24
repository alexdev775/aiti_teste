import pytest

@pytest.fixture
def numeros():
    return [1,2,3,4,5]

def soma_dobro(numeros):
    return sum(x*2 for x in numeros)

def test_soma_dobra(numeros):
    assert soma_dobro(numeros) == 30
