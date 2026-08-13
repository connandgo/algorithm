def solution(n, lost, reserve):
    los = set(lost) - set(reserve)
    res = set(reserve) - set(lost)
    answer = n - len(los)
    
    for l in sorted(los):
        if l-1 in res:
            res.remove(l-1)
            answer += 1
        elif l+1 in res:
            res.remove(l+1)
            answer += 1            
    return answer