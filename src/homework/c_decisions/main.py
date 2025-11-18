from decisions import get_letter_grade, get_options_ratio, get_faculty_rating

def main():
	try:
		option = float(input("Enter the number of options: "))
		total = float(input("Enter the total: "))
	except ValueError:
		print("Invalid input. Please enter numeric values.")
		return

	ratio = get_options_ratio(option, total)
	rating = get_faculty_rating(ratio)

	print(f"Ratio: {ratio:.2f}")
	print(f"Faculty Rating: {rating}")

if __name__ == "__main__":
	main()




print(f"MAIN MENU")
print(f"1 - Letter grade using if")
print(f"2 - Letter grade using switch")
print(f"3 - Exit")
option = input("Select an option (1, 2, or 3): ")

if option == "1":
    number = float(input("Enter a number between 0 and 100: "))
    if 0 <= number <= 100:
        print(f"Letter grade (if): {get_letter_grade(number)}")
    else:
        print("Number is out of range.")
if option == "2":
    number = float(input("Enter a number between 0 and 100: "))
    if 0 <= number <= 100:
        print(f"Letter grade (switch): {get_letter_grade(number)}")
    else:
        print("Number is out of range.")
if option == "3":
    print("Exiting program.")



