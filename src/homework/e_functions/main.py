import sys
sys.path.append("./")
from src.homework.e_functions.value_return import get_gross_pay, get_fica_tax, get_federal_tax
from src.homework.e_functions.void_func import display_payroll_check    

hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

gross_pay = get_gross_pay(hours, rate)
fica_tax = get_fica_tax(gross_pay)
federal_tax = get_federal_tax(gross_pay)

net_pay = gross_pay - fica_tax - federal_tax
display_payroll_check(gross_pay, fica_tax, federal_tax, net_pay)
net_pay = gross_pay - fica_tax - federal_tax