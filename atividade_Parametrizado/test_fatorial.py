import pytest
from fatorial import fatorial

@pytest.mark.parametrize("n,res",[(0,1), (1,1), (2,2), (3,6), (4,24), (5,120), (6,720)])

def test_fatorial(n,res):
    assert fatorial(n) == res 

@pytest.mark.parametrize("entrada_negativa", [-1,-2,-10])

def test_fatorial_negativo(entrada_negativa):
    with pytest.raises(RecursionError):
        fatorial(entrada_negativa)