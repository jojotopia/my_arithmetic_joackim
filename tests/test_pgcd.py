import pytest
from my_arithmetic_joackim import pgcd

def test_pgcd():
    # Tester des cas simples
    assert pgcd(12, 18) == 6
    assert pgcd(17, 23) == 1
    assert pgcd(36, 24) == 12
    assert pgcd(1, 1) == 1
    assert pgcd(2, 2) == 2