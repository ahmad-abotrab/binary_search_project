# tests/test_binary_search.py

import unittest
from src.binary_search import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_element_found(self):
        arr = [2, 3, 4, 10, 40]
        x = 10
        result = binary_search(arr, x)
        self.assertEqual(result, 3)

    def test_element_not_found(self):
        arr = [2, 3, 4, 10, 40]
        x = 5
        result = binary_search(arr, x)
        self.assertEqual(result, -1)

    def test_empty_array(self):
        arr = []
        x = 1
        result = binary_search(arr, x)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()
