from collections import deque

def solution(maps):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    # 시작 지점에서 레버를 당긴 후 통로로 이동해서 출구로 나가는데까지 걸리는 시간을 측정한다.
    # S O X L E 가있고 S 에서 출발해서 L로 갔다가 E로 가야돼
    # 일단 S를 찾고, 1차로 L까지 BFS를 돌리면서 cnt +1
    # L 부터 E 까지 2차로 Bfs를 돌리면서 +1
    # BFS를 두번 돌아야되니까 함수로 만드느게 좋겠다
    # 더이상 돌수가없는데 L이나 E를 발견 못하면 리턴 -1

    n = len(maps)
    m = len(maps[0])

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                sx, sy = i, j
            elif maps[i][j] == 'L':
                lx, ly = i, j

    def bfs(start_x, start_y, target):
        visited = [[False] * m for _ in range(n)]
        q = deque()
        q.append((start_x, start_y, 0))
        visited[start_x][start_y] = True

        while q:
            x, y, cnt = q.popleft()
            if maps[x][y] == target:
                return cnt
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                if maps[nx][ny] == 'X':
                    continue
                if visited[nx][ny]:
                    continue
                visited[nx][ny] = True
                q.append((nx, ny, cnt + 1))
        return -1
    first = bfs(sx, sy, 'L')
    if first == -1:
        return -1
    second = bfs(lx, ly, 'E')
    if second == -1:
        return -1
    return first + second