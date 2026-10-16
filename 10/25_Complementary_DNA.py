SYMBOLS = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

def complementary_dna(strand: str) -> str:
    complementary_strand = []
    for value in strand:
        complementary_strand.append(SYMBOLS[value])
    return "".join(complementary_strand)