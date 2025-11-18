import sys
sys.path.append("./")

from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget


def print_menu():
    print("\nInventory Menu\n")
    print("1-Add or Update Item")
    print("2-Delete Item")
    print("3-Exit")


def prompt_int(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Please enter a valid integer.")


def main():
    inventory = {}

    while True:
        print_menu()
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            name = input("Enter item name: ").strip()
            qty = prompt_int("Enter quantity (can be negative to reduce): ")
            try:
                add_inventory(inventory, name, qty)
                print(f"Inventory updated: {name} -> {inventory.get(name)}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            name = input("Enter item name to delete: ").strip()
            current = inventory.get(name, 0)
            if current == 0:
                print(f"Item '{name}' not found in inventory.")
            else:
                # remove entire item by removing current quantity
                removed = remove_inventory_widget(inventory, name, current)
                if removed:
                    print(f"Item '{name}' removed.")
                else:
                    print(f"Could not remove item '{name}'.")

        elif choice == "3":
            print("Exiting Inventory Menu. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()
