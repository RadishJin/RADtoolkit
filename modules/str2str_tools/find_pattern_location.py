import re

# 원하는 패턴을 위치로 찾아내는 함수
def find_pattern_location(pattern: str, sequence: str, regex : bool = False) -> list[int]:
    """
    원하는 패턴을 위치로 찾아내는 함수.
    regex를 True로 설정하면 정규식 또한 반영해준다.
    """

    # 예외
    if not pattern or not sequence:
        return []

    # 패턴 인식
    if regex:
        target = re.compile(pattern)
    else:
        pat = re.escape(pattern)
        target = re.compile(f'(?=({pat}))')  
     

    return [match.start() for match in target.finditer(sequence)]


# Simple test
# sequence = "GATATATGCATATACTT"
# pattern = "ATAT"
# loci = find_locus_location(pattern, sequence)
# print(loci)