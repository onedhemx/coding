import unittest
from calculations import Vichisl

class Vichisl:
    def factorial(self):
        
        n = int(input())

        factorial = 1

        for i in range(2, n+1):
            factorial *= i

        print(factorial)
        
        
    def stepen(self, a , b):
        a = float(input('введите основание '))
        b = float(input('введите показ степени'))
        
        res = a ** b
        
        print(F'{a} в степени {b} равно {res}')
        
    def c_calculation(self, Q, m, t):
        
        Q = int(input('введите Q'))
        m = int(input('введите m'))
        t = int(input('введите t'))
        c = Q/(m * t)
        print(c)
        
        
class TestCalculations(unittest.TestCase):
    def setUp(self):
        self.calc = Vichisl()

    def test_factorial(self):
        self.assertEqual(self.calc.factorial(7), 5040)
        self.assertEqual(self.calc.factorial(4), 24)

    def test_power(self):
        self.assertAlmostEqual(self.calc.power(4, 3), 64)
        self.assertAlmostEqual(self.calc.power(2, 8), 256)

    def test_c_calculation(self):
        self.assertAlmostEqual(self.calc.c_calculation(10, 2, 5), 1.0)
        self.assertAlmostEqual(self.calc.c_calculation(20, 4, 2), 2.5)

a = Vichisl()
