__author__ = 'k0emt'

import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):
    def test_add(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(1, 1), 2)


if __name__ == '__main__':
    unittest.main()
