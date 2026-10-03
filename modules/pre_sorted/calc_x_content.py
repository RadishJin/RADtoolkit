from typing import Iterable

# 어떤 서열의 원하는 문자들의 비율을 계산하는 함수
def calc_x_content(seq: str, x: Iterable[str]) -> float:

    # 예외
    if (not seq) or (not x):
        return 0.0

    # 타겟 문자의 개수
    num = sum(seq.count(i) for i in set(x))

    return num / len(seq)


# Simple Test
test = "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC"
print(calc_x_content(test, ('G','C')))