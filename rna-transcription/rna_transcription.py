def to_rna(dna_strand):
    rna_dict = {"C": "G", "G": "C", "T": "A", "A": "U"}

    rna_list = ""

    for i in dna_strand:
        rna_list += rna_dict.get(i)

    return rna_list
