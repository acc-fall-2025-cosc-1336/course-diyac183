import unittest

import sys
sys.path.append("./")
'''
The file at /src/homework/b_in_proc_out/output has 
the function get_number.
'''
from src.homework.b_in_proc_out.output import get_number
from src.homework.b_in_proc_out.output import multiply_numbers

from src.homework.b_in_proc_out.output import get_sales_tax_amount
from src.homework.b_in_proc_out.output import get_tip_amount

class Test_Config(unittest.TestCase):

    def test_get_number_1(self):
        #test that the function get_number returns 1
        self.assertEqual(1, get_number(1))
    
    def test_get_number_2(self):
        #test that the function get_number returns 2
        self.assertEqual(2, get_number(2))

    def test_multiply_numbers_1(self):
        #test that the function multiply_numbers returns 25
        self.assertEqual(25, multiply_numbers(5))
    
    def test_multiply_numbers_2(self):
        #test that the function multiply_numbers returns 49
        self.assertEqual(49, multiply_numbers(7))
    def test_get_sales_tax_amount(self):
        from src.homework.b_in_proc_out.output import get_sales_tax_amount
        self.assertAlmostEqual(6.75, get_sales_tax_amount(100))
        self.assertAlmostEqual(0, get_sales_tax_amount(0))
        self.assertAlmostEqual(3.375, get_sales_tax_amount(50))
    def test_get_tip_amount(self):
        from src.homework.b_in_proc_out.output import get_tip_amount
        self.assertAlmostEqual(15, get_tip_amount(100,0.15))
        self.assertAlmostEqual(0, get_tip_amount(100,0))
        self.assertAlmostEqual(10, get_tip_amount(50,0.20))