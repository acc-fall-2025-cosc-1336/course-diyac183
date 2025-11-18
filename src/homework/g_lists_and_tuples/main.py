from homework.g_lists_and_tuples.lists import get_p_distance_matrix
import sys
sys.path.append("./")
def prompt_sequences():
    """Prompt the user for number of sequences and each sequence string.

    Returns a list of sequences where each sequence is a list of characters.
    """
    while True:
        try:
            n = int(input("Enter number of sequences (1-10): ").strip())
            if 1 <= n <= 10:
                break
            print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid integer, try again.")

    sequences = []
    for i in range(1, n + 1):
        while True:
            s = input(f"Enter sequence #{i} (characters, e.g. TTTCCA): ").strip()
            if not s:
                print("Sequence cannot be empty.")
                continue
            sequences.append(list(s))
            break

    return sequences


def print_matrix(mat):
    for row in mat:
        print(" ".join(f"{v:.5f}" for v in row))


def main():
    while True:
        print("\n1-Get p distance matrix")
        print("2-Exit")
        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == "1":
            try:
                seqs = prompt_sequences()
                mat = get_p_distance_matrix(seqs)
                print("\nP-distance matrix:")
                print_matrix(mat)
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()

