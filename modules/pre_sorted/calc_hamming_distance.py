# 문자열의 해밍 디스턴스 구하는 함수
def calc_hamming_distance(str1: str, str2: str) -> int:

    if len(str1) != len(str2):
        raise ValueError("두 문자열의 길이가 같아야 합니다.")

    return sum(c1 != c2 for c1, c2 in zip(str1, str2))


# Simple Test
# test1 = "GAGCCTACTAACGGGAT"
# test2 = "CATCGTAATGACGGCCT"
# print(calc_hamming_distance(test1, test2))  # 출력: 7

