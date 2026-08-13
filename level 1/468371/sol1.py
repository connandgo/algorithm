import math

def lcm(a,b):
    return abs(a*b) // math.gcd(a,b)

def solution(signals):
    cycles = []
    # 주기 구하기
    for G, Y, R in signals:
        cycles.append(G+Y+R)
    k = 1
    # 최소공배수 구하기 
    for cycle in cycles:
        k = lcm(k,cycle)
    # 배열 만들기
    sets = []
    for G,Y,R in signals:
        cycle = G+Y+R
        s = set()
        for start in range(G+1, G+Y+1):
            i = start
            while i <= k:
                s.add(i)
                i += cycle
        sets.append(s)
    # 공통된 수 구하기
    common = sets[0]
    for i in range(1, len(sets)):
        common = common & sets[i]
        
    return min(common) if common else -1