import sys
sys.path.append("./")
from src.homework.h_strings.strings import get_hamming_distance, get_dna_complement

def main():
    while True:
        print("\n1-Hamming Distance")
        print("2-Dna Complement")
        print("3-Exit")
        
        choice = input("Select an option (1, 2, or 3): ")
        
        if choice == '1':
            dna1 = input("Enter the first DNA string: ")
            dna2 = input("Enter the second DNA string: ")
            try:
                distance = get_hamming_distance(dna1, dna2)
                print(f"Hamming Distance: {distance}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '2':
            dna = input("Enter a DNA string: ")
            complement = get_dna_complement(dna)
            print(f"DNA Complement: {complement}")
        
        elif choice == '3':
            print("Exiting program.")
            sys.exit()
        
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()