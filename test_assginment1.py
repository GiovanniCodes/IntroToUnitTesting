import unittest
from Assignment1 import retirement, splitAmount


class TestSplitAmount(unittest.TestCase):
    def test_retire_value_error(self):
        self.assertRaises(ValueError,retirement, g,'g',8,'f')
    def test_retire_amount(self):
        self.assertAlmostEqual(retirement(44,10000,10,20000),59)
    def test_retire_right(self):
        self.assertAlmostEqual(retirement(44,0,10,20000), "Dead")
    def test_retire_wrong(self):
        self.assertNotEqual(retirement(44,10000,10,20000), 70)
    def test_split_amount(self):
        self.assertAlmostEqual(splitAmount(20,5),[4.6,4.6,4.6,4.6,4.6])
    def test_split_right(self):
        self.assertAlmostEqual(splitAmount(20, 1), [23.0])
    def test_split_wrong(self):
        self.assertNotEqual(splitAmount(20, 1), [2])
    def test_split_value_error(self):
        self.assertRaises(ValueError,splitAmount, 6 ,'g');