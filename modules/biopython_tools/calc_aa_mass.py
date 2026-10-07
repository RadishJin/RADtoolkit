from Bio.Data import IUPACData
from typing import Iterable

# Canonical AminoAcid에 대해서 Monoisotopic Molar Mass 구하는 함수
def calc_canonical_aa_monoiso_mass(sequence: Iterable) -> float:
    """
    Canonical AminoAcid에 대해서 Monoisotopic Molar Mass 구하는 함수
    """

    mass = sum(IUPACData.monoisotopic_protein_weights[i] for i in sequence)

    monoiso_h = 1.00782503223
    monoiso_o = 15.99491461957

    water = monoiso_h*2 + monoiso_o

    dehydration = (len(sequence) - 1) * water

    return mass - dehydration