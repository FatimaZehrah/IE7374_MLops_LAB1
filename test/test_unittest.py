import unittest
from src.calculator import fun1, fun2, fun3, fun4, fun5


class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(fun1(2, 3), 5)

    def test_fun2(self):
        self.assertEqual(fun2(10, 4), 6)

    def test_fun3(self):
        self.assertEqual(fun3(3, 5), 15)

    def test_fun4(self):
        self.assertEqual(
            fun4(2, 3),
            (2 + 3) + (2 - 3) + (2 * 3)
        )

    def test_fun5_division(self):
        self.assertEqual(fun5(10, 2), 5)

    def test_fun5_divide_by_zero(self):
        with self.assertRaises(ValueError):
            fun5(10, 0)


if __name__ == "__main__":
    unittest.main()
