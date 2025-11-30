import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # ----------------- ADDITION TESTS -----------------
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_add_positive_and_negative(self):
        self.assertEqual(self.calc.add(-2, 5), 3)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)

    # ----------------- SUBTRACTION TESTS -----------------
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -2), -3)

    def test_subtract_mixed_numbers(self):
        self.assertEqual(self.calc.subtract(-3, 7), -10)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    # ----------------- MULTIPLICATION TESTS -----------------
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-4, -5), 20)

    def test_multiply_mixed_numbers(self):
        self.assertEqual(self.calc.multiply(-3, 6), -18)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(10, 0), 0)

    # ----------------- DIVISION TESTS -----------------
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_divide_mixed_numbers(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_divide_zero_by_number(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

# Run the tests
if __name__ == "__main__":
    unittest.main()
