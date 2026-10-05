import io

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
            seq[current_id].append(line)
    
    return {seq_id: "".join(chunks) for seq_id, chunks in seq.items()}


# Simple test
# test = """
# >Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
# TCCCACTAATAATTCTGAGG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
# ATATCCATTTGTCAGCAGACACGC
# >Rosalind_0808
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
# TGGGAACCTGCGGGCAGTAGGTGGAAT
# """
# print(parse_rosalind_fasta(test))







