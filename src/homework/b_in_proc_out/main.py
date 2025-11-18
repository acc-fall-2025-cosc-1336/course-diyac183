import output

x=output.multiply_numbers(5)
print(x)
print("\n")
x=output.multiply_numbers(7)
print(x)
print("\n")
x=output.multiply_numbers(8)
print(x)
print("\n")

#The program must prompt the users for keyboard data for the meal amount and tip rate.
#(Make it clear in the user prompt whether decimal or whole number is required for the tip amount)

#Use the functions get_sales_tax_amount and get_tip_amount.
#Display a receipt (formatting the number decimal spaces is optional): 
#    Meal Amount:      20
#    Sales Tax:             1.35       
#    Tip Amount:      3
#    Total:                   24.35
meal_amount=float(input("Enter the meal amount: "))
tip_rate=float(input("Enter the tip rate as a decimal (e.g., 0.15 for 15%): "))
sales_tax=output.get_sales_tax_amount(meal_amount)
tip_amount=output.get_tip_amount(meal_amount,tip_rate)
total=meal_amount+sales_tax+tip_amount
print(f"\nReceipt:")
print(f"Meal Amount: {meal_amount:.2f}")
print(f"Sales Tax: {sales_tax:.2f}")
print(f"Tip Amount: {tip_amount:.2f}")
print(f"Total: {total:.2f}")
print("\n")
