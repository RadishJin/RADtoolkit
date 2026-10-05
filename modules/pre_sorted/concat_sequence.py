# 두 문자열의 가장 짧은 합친 문자열과 오버랩 길이를 반환하는 함수
def concat_shortest(seq1: str, seq2: str) -> tuple[str, int]:
    """
    두 문자열의 가장 짧은 합친 문자열과 오버랩 길이를 반환하는 함수
    """

    len1, len2 = len(seq1), len(seq2)
    max_k = min(len1, len2)

    # 완전 포함 경우 제외
    if seq2 in seq1:
        return (seq1, len(seq2))
    if seq1 in seq2:
        return (seq2, len(seq1))

    # prefix, suffix overlap racing
    for k in range(max_k, 0, -1):
        match_prefix = seq1[-k:] == seq2[:k]
        match_suffix = seq1[:k] == seq2[-k:]

        if match_prefix and match_suffix:
            return (seq1 + seq2[k:], k)
        elif match_prefix:
            return (seq1 + seq2[k:], k)
        elif match_suffix:
            return (seq2 + seq1[k:], k)
        
    return (seq1 + seq2, 0)


# 유향성 문자열 합치기, 이후 합친 문자열과 오버랩 길이 반환
def concat_directed(seq1 : str, seq2 : str) -> tuple[str, int]:
    """
    유향성 문자열 합치기, 이후 합친 문자열과 오버랩 길이 반환
    """

    max_k = min(len(seq1), len(seq2))

    for k in range(max_k, 0, -1):
        if seq1[-k:] == seq2[:k]:
            return (seq1 + seq2[k:], k)

    return (seq1 + seq2, 0)    


# 원하는 방향으로, 원하는 수만큼 겹치는지 판단하고, 겹친다면 합친 문자열 반환, 겹치지 않으면 빈 문자열 반환
def concat_custom(seq1 : str, seq2 : str, overlap_len : int) -> str:
    """
    원하는 방향으로, 원하는 수만큼 겹치는지 판단하고, 겹친다면 합친 문자열 반환, 겹치지 않으면 빈 문자열 반환
    """

    if seq1[-overlap_len:] == seq2[:overlap_len]:
        return (seq1 + seq2[overlap_len:])
    else:
        return ""