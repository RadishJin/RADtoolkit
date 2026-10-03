import numpy as np

# MSA 각 성분 빈도를 ndarray로 반환해주는 함수
def calc_profile(matrix: np.ndarray) -> np.ndarray:

    # base mapping
    base = np.array(['A', 'C', 'G', 'T'])

    # 3차원 불리언 마스킹 이후 개수 반환
    profile = (base[:, None, None] == matrix).sum(axis = 1)

    return profile


# Consensus Sequence
def find_consensus(matrix: np.ndarray) -> str:

    # base mapping
    base = np.array(['A', 'C', 'G', 'T'])

    # profile loading
    profile = calc_profile(matrix)

    # Consensus 생성
    consensus_indices = np.argmax(profile, axis=0)
    consensus_seq = "".join(base[consensus_indices])

    return consensus_seq



# Simple Test
test = np.array([['A', 'T', 'C', 'C', 'A', 'G', 'C', 'T'],
['G', 'G', 'G', 'C', 'A', 'A', 'C', 'T'],
['A', 'T', 'G', 'G', 'A', 'T', 'C', 'T'],
['A', 'A', 'G', 'C', 'A', 'A', 'C', 'C'],
['T', 'T', 'G', 'G', 'A', 'A', 'C', 'T'],
['A', 'T', 'G', 'C', 'C', 'A', 'T', 'T'],
['A', 'T', 'G', 'G', 'C', 'A', 'C', 'T']])
if __name__ == '__main__':
    print(calc_profile(test))
    print(find_consensus(test))