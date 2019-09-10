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
        
    def test_bmi_overweight(self):
        self.assertEqual(bmiCalc(72, 200), "Overweight")
    def test_bmi_underweight(self):
        self.assertEqual(bmiCalc(72, 105), "Underweight")
    def test_bmi_normal(self):
        self.assertEqual(bmiCalc(72, 170), "Normal")
    def test_bmi_obese(self):
        self.assertEqual(bmiCalc(72, 480), "Obese")
    def test_bmi_value_error(self):
        self.assertRaises(ValueError, bmiCalc, 'a', 'b', 'c')
    def test_bmi_negative(self):
        self.assertEqual(bmiCalc(72, -180), "Negative")
    def test_distance_zero(self):
        self.assertEqual(shortestDistance(1,1,1,1), 0)
    def test_distance_one(self):
        self.assertAlmostEqual(shortestDistance(1,1,2,2), 1)
    def test_distance_one(self):
        self.assertAlmostEqual(shortestDistance(5,10,25,3), 21)
