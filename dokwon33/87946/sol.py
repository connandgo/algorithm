# permutation....마렵다

def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    visited = [False] * n
    # fi : 현재 피로도 , count : 탐색 수
    def dfs(fi, count):
        nonlocal answer
        answer = max(answer, count)
        for i in range(n):
            if not visited[i] and fi >= dungeons[i][0]:
                visited[i] = True
                dfs(fi - dungeons[i][1], count + 1)
                visited[i] = False
    dfs(k, 0)
    return answer