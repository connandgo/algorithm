from collections import defaultdict
def solution(clothes):
    answer = 1
    clo_dict = defaultdict(int)
    for a, b in clothes:
        clo_dict[b] += 1
    
    for v in clo_dict.values():
        answer *= v + 1
    return answer - 1