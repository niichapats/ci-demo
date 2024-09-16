from unittest import TestCase
from statistics import variance, stdev
from math import sqrt

class StatisticsTest(TestCase):

    def test_variance_typical_values(self):
        """variance of typical values"""
        self.assertEqual(0.0, variance([10.0,10.0,10.0,10.0,10.0]))
        self.assertEqual(2.0, variance([1,2,3,4,5]))
        self.assertEqual(8.0, variance([10,2,8,4,6]))

    def test_variance_non_integers(self):
        """variance should work with decimal values"""
        # variance([x,y,z]) == variance([x+d,y+d,z+d]) for any d
        self.assertAlmostEqual(4.0, variance([0.1, 4.1]))
        # variance([0,4,4,8]) == 8
        self.assertAlmostEqual(8.0, variance([0.1, 4.1, 4.1, 8.1]))

    def test_stdev(self):
        """standard deviation tests"""
        # standard deviation of a single value should be zero
        self.assertEqual(0.0, stdev([10.0]))
        # simple test
        self.assertEqual(2.0, stdev([1, 5]))
        # variance([0, 0.5, 1, 1.5, 2.0]) is 0.5
        self.assertEqual(sqrt(0.5), stdev([0, 0.5, 1, 1.5, 2]))

    def test_average_typical_values(self):
        """Test average with typical values"""
        from statistics import average  # Importing average from the module where it is defined
        self.assertEqual(3.0, average([1, 2, 3, 4, 5]))  # Average of [1, 2, 3, 4, 5] is 3.0
        self.assertEqual(5.0, average([5, 5, 5, 5, 5]))  # Average of all same numbers
        self.assertAlmostEqual(2.6667, average([2, 2, 4]), places=4)  # Test for decimals

    def test_average_empty_list(self):
        """Test that average raises ValueError for empty list"""
        from statistics import average  # Importing average from the module where it is defined
        with self.assertRaises(ValueError):
            average([])  # Should raise ValueError

    def test_variance_raise_error(self):
        """Test that variance raises ValueError for empty list"""
        with self.assertRaises(ValueError):
            variance([])  # Should raise ValueError
