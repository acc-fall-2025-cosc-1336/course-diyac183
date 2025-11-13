def main():
    """Main program to manage a list and display low/high values"""
    values = []
    
    while True:
        # Display menu
        print("\n1-Show the list low/high values")
        print("2-Exit")
        choice = input("Enter your choice (1 or 2): ").strip()
        
        if choice == "1":
            # Enter list values
            while True:
                value = input("Enter a list value: ").strip()
                
                # Try to convert to a number
                try:
                    values.append(float(value))
                except ValueError:
                    print("Please enter a valid number.")
                    continue
                
                # Ask if user wants to enter another value (only after at least 3 values)
                if len(values) >= 3:
                    another = input("Do you want to enter another value? ").strip().lower()
                    if another != "y" and another != "yes":
                        break
            
            # Display the low and high values
            if values:
                print(f"\nLowest value: {min(values)}")
                print(f"Highest value: {max(values)}")
        
        elif choice == "2":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

