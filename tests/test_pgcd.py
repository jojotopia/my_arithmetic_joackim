from unittest import TestCase
from my_arithmetic_joackim.pgcd import pgcd

class TestFunctions(TestCase):

    def test_pgcd(self):
        self.assertEqual(8, pgcd(56,48))

    def test_pgcd(self):
        self.assertEqual(2, pgcd(2,4))
