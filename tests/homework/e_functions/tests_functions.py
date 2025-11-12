import sys
from homework.e_functions.value_return import get_gross_pay
sys.path.append("./")
get_gross_pay
def test_get_gross_pay():
    assert get_gross_pay(45, 10) == 475
    assert get_gross_pay(40, 10) == 400
    assert get_gross_pay(30, 10) == 300

import sys
from homework.e_functions.value_return import get_fica_tax
sys.path.append("./")

def test_get_fica_tax():
    assert get_fica_tax(475) == 36.4875
    assert get_fica_tax(400) == 30.6
    assert get_fica_tax(300) == 22.95

import sys
from homework.e_functions.value_return import get_federal_tax
sys.path.append("./")

def test_get_federal_tax():
    assert get_federal_tax(475) == 38.0
    assert get_federal_tax(400) == 32.0
    assert get_federal_tax(300) == 24.0