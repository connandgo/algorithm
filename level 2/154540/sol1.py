from collections import deque
def solution(maps):
    # 기본 설정 어우 많아~
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    answer = []
    q = deque()
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'X' or visited[i][j]:
                continue
            # 새로운 섬 발견 한겨
            q.append((i,j))
            visited[i][j] = True
            cnt = int(maps[i][j])
            while q:
                # bfs 돌려
                x, y = q.popleft()
                for dir in range(4):
                    idx = x + dx[dir]
                    idy = y + dy[dir]
                    if not (0 <= idx < len(maps) and 0 <= idy < len(maps[0])):
                        continue
                    if not visited[idx][idy] and maps[idx][idy] != 'X':
                        q.append((idx,idy))
                        visited[idx][idy] = True
                        cnt += int(maps[idx][idy])
            answer.append(cnt)         
    return sorted(answer) if answer else [-1]

