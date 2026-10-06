# 여러 서열에 공통으로 존재하는 가장 긴 모티프(LCSM) 중 하나를 반환한다.
def find_only_motif(seqlist : list) -> str:
    """
    여러 서열에 공통으로 존재하는 가장 긴 모티프(LCSM) 중 하나를 반환한다.
    """

    # 원본 보호
    seq_list = seqlist.copy()

    # 가장 짧은 strand를 main으로 처리하고, 나머지 문자열 짧은 순서대로 리스트화
    main = min(seq_list, key = len)
    seq_list.remove(main)
    seq_list = sorted(seq_list, key= lambda x: len(x))

    # 가장 긴 공통부분 찾기
    test = ""
    found_motif = ""
    for sub_len in range(len(main), 0, -1):
        for start in range(len(main) - sub_len + 1):
            test = main[start : start + sub_len]
            if all(test in seq for seq in seq_list):
                found_motif = test
                break
        if found_motif:
            break

    return found_motif