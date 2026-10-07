import io
import time
import requests


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
            parts = line.split("|")

            if len(parts) >= 2:
                current_id = parts[1].strip()
                
            else:
                current_id = line[1:].split()[0].strip()
            seq[current_id] = []

        else:
            if current_id:
                seq[current_id].append(line)

    return {seq_id: "".join(chunks) for seq_id, chunks in seq.items()}


# UniProt FASTA IO
def io_uniprot_fasta(id_list : list[str]) -> tuple[str, list[str]]:
    """
    UniProt Accession ID를 리스트로 입력하면
    해당 ID의 FASTA 전체를 읽어옴

    튜플 ( 읽은 파스타, 누락 id 리스트 ) 로 출력함
    """
    headers = {"User-Agent" : "Mozilla/5.0"}

    if not id_list:
        return ("", [])

    fasta_list = []
    omit_list = []
    for acc_id in id_list:
        url = f"https://www.uniprot.org/uniprot/{acc_id}.fasta"
        response = requests.get(url, headers = headers, timeout= 10)

        if response.status_code == 200 and response.text.startswith('>'):
            fasta_list.append(response.text.strip())

        else:
            print(f"[Warning] Fasta Data Omitted : {acc_id}")
            omit_list.append(acc_id)

        time.sleep(0.05)

    return ("\n\n".join(fasta_list), omit_list)
