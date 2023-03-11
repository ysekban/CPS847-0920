import unittest
from function import cps0920

class TestSampleMethods(unittest.TestCase):
    """
    Test harness
    """

    def test(self):
        """
        Test increments
        """
        self.assertEqual(cps0920(7), 70)

if __name__ == '__main__':
    unittest.main()
