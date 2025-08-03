#https://github.com/oscarmartinez0806/lab10-OM-RG
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
     def test_add(self): # 3 assertions
         self.assertEqual(add(1, 2), 3)
         self.assertEqual(add(-2, 2), 0)
         self.assertEqual(add(1, 3), 4)

     def test_subtract(self): # 3 assertions
         self.assertEqual(sub(6, 2), 4)
         self.assertEqual(sub(9, 4), 5)
         self.assertEqual(sub(9, 10), -1)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2,4), 8)
        self.assertEqual(mul(-3, 4), -12)
        self.assertEqual(mul(0, 5), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(5, 10), 2.0)
        self.assertAlmostEqual(div(5, 1), 0.2)
        with self.assertRaises(ZeroDivisionError):
            div(0, 3)
    # ##########################

    ######## Partner 2
     def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
          with self.assertRaises(ZeroDivisionError):
               div(0, 5)

     def test_logarithm(self): # 3 assertions
         self.assertAlmostEqual(log(5, 125), 3)
         self.assertAlmostEqual(log(3, 27), 3)
         self.assertAlmostEqual(log(6, 36), 2)

     def test_log_invalid_base(self): # 1 assertion
         with self.assertRaises(ValueError):
             log(1, 10)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(1,10)
        with self.assertRaises(ValueError):
            log(0,10)
        with self.assertRaises(ValueError):
            log(2, -5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(-3, -4), 5.0)

    def test_sqrt(self): # 3 assertions
        self.assertAlmostEqual(square_root(16), 4.0)
        self.assertAlmostEqual(square_root(0), 0.0)
        with self.assertRaises(ValueError):
            square_root(-4)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()