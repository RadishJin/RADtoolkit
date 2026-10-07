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


# 타겟 안에서 원하는 패턴을 가진 문자열들을 리스트로 뽑아주는 함수
def find_pattern(pattern: str, sequence: str) -> list[str]:
    """
    원하는 패턴을 Regex로 넣어주면
    타겟에서 해당 패턴을 가진 모든 문자열을 리스트로 반환한다.
    """

    # 예외
    if not pattern or not sequence:
        return []

    try:
        target = re.compile(pattern)
    except re.error as e:
        raise ValueError(f"올바르지 않은 정규표현식 패턴입니다: {e}")

    result = []
    for i in range(len(sequence)):
        match = target.match(sequence, pos= i)
        if match and match.group():
            result.append(match.group())

    return result


# Simple test
# sequence = "GATATATGCATATACTT"
# pattern = "ATAT"
# loci = find_locus_location(pattern, sequence)
# print(loci)