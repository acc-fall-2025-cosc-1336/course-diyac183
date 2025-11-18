TAX_RATE = 0.0675  # 6.75%

def get_number(num):
    return num

def multiply_numbers(num):
    return num*num

def get_sales_tax_amount(meal_amount:float)->float:
    return meal_amount*TAX_RATE

def get_tip_amount(meal_amount,tip_rate:float)->float:
    return meal_amount*tip_rate



