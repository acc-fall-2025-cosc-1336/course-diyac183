import sys

# import decisions

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def sum_odd_numbers(n):
    return sum(i for i in range(1, n + 1) if i % 2 == 1)

def get_valid_int(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val < value < max_val:
                return value
            else:
                print(f"Please enter a number greater than {min_val} and less than {max_val}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    while True:
        print("1-Factorial")
        print("2-Sum odd numbers")
        print("3-Exit")
        choice = input("Select an option: ")
        if choice == '1':
            num = get_valid_int("Enter a number (1-9): ", 0, 10)
            print(f"Factorial of {num} is {factorial(num)}")
        elif choice == '2':
            num = get_valid_int("Enter a number (1-99): ", 0, 100)
            print(f"Sum of odd numbers up to {num} is {sum_odd_numbers(num)}")
        elif choice == '3':
            print("Exiting program.")
            sys.exit()
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()


