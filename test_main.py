import unittest
from main import add

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(3, 3), 7)

if __name__ == '__main__':
    unittest.main()
