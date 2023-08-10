import unittest

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

class TestCalculator(unittest.TestCase):
    # utilizamos 'SetUp' para crear una instancia de 'Calculator'
    def setUp(self):
        self.calculator = Calculator()

    # método ejecutado después de cada prueba, se encargará de eliminar la instancia de 'Calculator', garantiza la limpieza adecuada después de cada prueba.
    def tearDown(self):
        del self.calculator
    
    def test_add(self):
        result = self.calculator.add(3, 5)
        self.assertEqual(result, 8)
    
    def test_subtract(self):
        result = self.calculator.subtract(10, 4)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()

# python -m unittest discover