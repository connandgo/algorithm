from collections import Counter

def solution(participant, completion):
    par = Counter(participant)
    com = Counter(completion)
    par = par - com
    return list(par.keys())[-1]