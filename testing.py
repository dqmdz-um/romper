import unittest

from suma import suma

class TestSuma(unittest.TestCase):

    def test_suma(self):
        resultado = suma(2, 3)
        self.assertEqual(resultado, 5)

if __name__ == "__main__":
    unittest.main()