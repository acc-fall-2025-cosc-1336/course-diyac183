from decisions import get_options_ratio, get_faculty_rating

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
