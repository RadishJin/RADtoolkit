import re

# base sequence에서 원하는 패턴을 위치로 찾아내는 함수
def find_locus_location(pattern: str, sequence: str) -> list[int]:

    # 예외
    if not pattern or not sequence:
        return []

    # 준비물
    loci = []

    # 패턴 인식
    target = re.compile(f'(?=({pattern}))')    

    return [match.start() for match in target.finditer(sequence)]


# Simple test
# sequence = "GATATATGCATATACTT"
# pattern = "ATAT"
# loci = find_locus_location(pattern, sequence)
# print(loci)