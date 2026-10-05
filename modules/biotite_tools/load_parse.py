import gzip                                 # .gz 압축된 파일 읽기용
import biotite.structure.io.pdbx as pdbx    # .cif 파일 읽기용
import biotite.structure as struc           # 텍스트 파일 파싱용


# cif.gz 파일을 AtomArray로 읽어오는 함수
def load_structure(id: str) -> struc.AtomArray:

    with gzip.open(f"raw_dataset/{id}.cif.gz", "rt", encoding = "utf-8") as f:
        raw = pdbx.CIFFile.read(f)

    atoms = pdbx.get_structure(raw, model= 1)

    return atoms


# 백본 아톰만 남기는 파서
def parse_bb(atoms : struc.AtomArray) -> struc.AtomArray:

    # Biotite.structure 이용 residue와 관련된 원자만 남기기 (비표준 아미노산도 포함)
    residue_mask = struc.filter_amino_acids(atoms)
    residue_atom = atoms[residue_mask]

    # Backbone atoms
    is_backbone = struc.filter_peptide_backbone(residue_atom)
    bb_atoms = residue_atom[is_backbone]
    # print(bb_atoms)

    return bb_atoms


# 알파카본만 남기는 파서
def parse_ca(atoms : struc.AtomArray) -> struc.AtomArray:

    # Residue Atom Boolean Masking
    residue_mask = struc.filter_amino_acids(atoms)
    residue_atom = atoms[residue_mask]

    # Alpha Carbon Boolean Masking
    is_ca = (residue_atom.get_annotation("atom_name") == "CA")
    ca_atoms = residue_atom[is_ca]

    return ca_atoms