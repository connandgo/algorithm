# DFS + 메모이제이션
# 완전탐색 DFS와 구조는 동일하고 "(인덱스, 누적합)" 상태를 캐싱하는 로직만 추가
from functools import lru_cache


def solution(numbers, target):
    n = len(numbers)

    # 상태를 (idx, total) 튜플로 잡는 것이 핵심.
    # total만으로 캐싱하면 남은 숫자가 다른 상황을 같은 상태로 착각한다.
    @lru_cache(maxsize=None)
    def dfs(idx, total):
        if idx == n:      # 숫자를 다 썼을 때만 종료
            return 1 if total == target else 0
        return dfs(idx + 1, total + numbers[idx]) + dfs(idx + 1, total - numbers[idx])

    answer = dfs(0, 0)
    dfs.cache_clear()    # 다음 호출에 캐시가 새지 않도록 정리
    return answer
