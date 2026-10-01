from collections import Counter

# base sequence(str type)의 base 개수를 세는 함수
def count_base(seq: str) -> dict[str, int]:

    # 대문자로 정규화
    seq = seq.upper()

    # Counter를 이용하여 각 base의 개수를 세어 딕셔너리에 저장
    base_counted = Counter(seq)

    return dict(base_counted)

# Simple Test
# test = count_base("AGCTAGCTAGCTAGCTAASDKFJAKENRMAEJRGDHAKNDSNGGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCT")
# print(test)
