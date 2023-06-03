import unittest
from main import add

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        result = add(1, 2)
        self.assertEqual(result, 3, "Addition result is incorrect")

    def test_add_fail(self):
        result = add(1, 2)
        self.assertEqual(result, 4, "Addition result is incorrect")

    def test_add_fail2(self):
        result = add(1, 2)
        self.assertEqual(result, 5, "Addition result is incorrect")
if __name__ == '__main__':
    unittest.main()
