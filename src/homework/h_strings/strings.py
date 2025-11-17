#Must use loops only; no Python built in functionality(NO STRING SLICING).

def get_hamming_distance(dna1, dna2):
    """
    Calculates the Hamming distance between two DNA strings of equal length.
    
    Args:
        dna1 (str): The first DNA string.
        dna2 (str): The second DNA string.
    
    Returns:
        int: The Hamming distance between dna1 and dna2.
    
    Raises:
        ValueError: If the input strings have different lengths.
    """
    if len(dna1) != len(dna2):
        raise ValueError("Strings must be of equal length for Hamming distance.")
    
    distance = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            distance += 1
    return distance

def get_dna_complement(dna):
    """
    Returns the DNA complement of a given DNA string.
    A complements with T, and G complements with C.
    
    Args:
        dna (str): The DNA string.
    
    Returns:
        str: The complement DNA string.
    """
    complement = ""
    for i in range(len(dna)):
        if dna[i] == 'A':
            complement += 'T'
        elif dna[i] == 'T':
            complement += 'A'
        elif dna[i] == 'G':
            complement += 'C'
        elif dna[i] == 'C':
            complement += 'G'
    return complement