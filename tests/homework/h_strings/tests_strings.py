import unittest 
import sys
sys.path.append("./")
from src.homework.h_strings.strings import get_hamming_distance
from src.homework.h_strings.strings import get_dna_complement
class Test_Config(unittest.TestCase):
    def test_get_hamming_distance(dna2):
        my_string = "GAGCCTACTAACGGGAT"
        dna2.assertEqual(get_hamming_distance("GAGCCTACTAACGGGAT"))
        dna2.assertEqual(get_hamming_distance("CATCGTAATGACGGCCT"), 7)

    def test_get_dna_complement(dna2):
        dna2.assertEqual(get_dna_complement("AAAACCCGGT"))
        dna2.assertEqual(get_dna_complement("ACCGGGTTTT"))
