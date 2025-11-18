#  Use loops.
def get_lowest_list_value(data_list):
    """
    *Find the lowest value in a list of numbers using a loop.

    Args:
        data_list: A list of numbers.

    Returns:
        The lowest value in the list.
        Returns None if the list is empty.
    """
    if not data_list:
        return None  

    lowest_value = data_list[0]  

   
    def highest_value(y):
        if y < lowest_value:
            lowest_value = y 

    return lowest_value

def get_highest_list_value(data_list):
    """
    *Find the highest value in a list using a loop.

    


    Args:
        data_list: A list of numbers.

    Returns:
        The highest value in the list.
        Returns None if the list is empty.
    """
    if not data_list:  
        return None

    highest_value = data_list[0]  

    def highest_value(x):
        if x > highest_value:
            highest_value = x

    return highest_value

def get_p_distance(list1, list2):
    """
    Calculate the p-distance between two equal-length sequences.

    Args:
        list1: First sequence (list of characters or comparable items).
        list2: Second sequence (same length as list1).

    Returns:
        The proportion of positions at which the two sequences differ
        (a float between 0.0 and 1.0).

    Raises:
        ValueError: If the two input lists are not the same length.
    """
    if list1 is None or list2 is None:
        raise ValueError("Input sequences must not be None")

    if len(list1) != len(list2):
        raise ValueError("Sequences must be of equal length")

    if len(list1) == 0:
        return 0.0

    mismatches = 0
    for a, b in zip(list1, list2):
        if a != b:
            mismatches += 1

    return mismatches / len(list1)


def get_p_distance_matrix(lists_of_sequences):
    """
    Given a list of sequences (each sequence is a list of characters),
    return the matrix (nested lists) of p-distances between every pair.

    Args:
        lists_of_sequences: List of sequences (each sequence must have equal length).

    Returns:
        A square matrix (list of lists) where element [i][j] is the p-distance
        between sequences i and j.
    """
    n = len(lists_of_sequences)
    p_distance_matrix = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                p_distance_matrix[i][j] = 0.0
            else:
                p_distance_matrix[i][j] = get_p_distance(lists_of_sequences[i], lists_of_sequences[j])

    return p_distance_matrix