import io
import re


# Module-Level variable
ACC_REGEX = re.compile(r'[A-Z][0-9][A-Z0-9]{3,7}(?:-[0-9]+)?')


# Rosalind 전용 fasta parser
def parse_rosalind_fasta(raw: str) -> dict:
    """
    Rosalind 전용 fasta parser
    """

    seq = {}
    current_id = ""

    for line in io.StringIO(raw):

        # 앞뒤 공백 제거
        line = line.strip()

        # 빈 줄은 패스
        if not line:
            continue

        # ID line이면 current_id를 갱신하고 seq 딕셔너리에 빈 문자열을 할당
        if line.startswith(">"):
            current_id = line[1:]
            seq[current_id] = []

        # sequence line이면 현재 ID에 해당하는 문자열에 이어붙이기
        else:
            if current_id:
                seq[current_id].append(line)
    
    return {seq_id: "".join(chunks) for seq_id, chunks in seq.items()}


# Uniprot fasta -> seq_dict       
def parse_uniprot_fasta(raw: str) -> dict[str, str]:
    """
    UniProt fasta를 넘기면
    accession id : fasta 형태로 딕셔너리화 하여 반환
    """
    seq = {}
    current_id = ""
    un = 0
    for line in io.StringIO(raw):
        line = line.strip()

        if not line:
            continue

        if line.startswith(">"):
            match = ACC_REGEX.search(line)

            if match:
                current_id = match.group()

            else:
                current_id = f'unknown_{un}'
                un += 1

            seq[current_id] = []

        else:
            if current_id:
                seq[current_id].append(line)

    return {seq_id: "".join(chunks) for seq_id, chunks in seq.items()}





