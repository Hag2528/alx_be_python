import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method
    def test_subtraction(self):
        """Return the subtraction of b from a."""
        self.assertEqual(self.calc.subtract(30,9),21)
        self.assertEqual(self.calc.subtract(-6,1),-7)    

    def test_multiplication(self):
       self.assertEqual(self.calc.multiply(10,30),300)
       self.assertEqual(self.calc.multiply(-2,-7),14)

    def test_division(self):
        self.assertEqual(self.calc.divide(54,3),18)
        self.assertEqual(self.calc.divide(72,8),9)
if __name__ == '__main__':
  unittest.main()