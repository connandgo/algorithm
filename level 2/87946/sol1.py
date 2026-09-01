def solution(k, dungeons):
    #완전탐색을 한다하면 N!인데 최대 8이니까 완탐이 가능하다 생각함
    #모든경우를 뒤져보면서 max를 return
    #순서가 없으니까 visited 리스트가 필요하다.
    visited = [False] * len(dungeons)
    def dfs(heart, count):
        best = count
        for i in range(len(dungeons)):
            if not visited[i]:
                if heart >= dungeons[i][0]:
                    visited[i] = True
                    result = dfs(heart - dungeons[i][1], count + 1)
                    best = max(best, result)
                visited[i] = False
        return best
    return dfs(k,0)