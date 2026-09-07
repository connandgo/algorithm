from collections import deque
# DEQUE말고는 모르겠어

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    def find_position(char):
        # maps 안에서 특정 문자가 있는 좌표를
        for row in range(n):
            for col in range(m):
                if maps[row][col] == char:
                    return row, col
        return None

    def bfs(start, target_char):
        # start 위치에서 target_char 칸까지 최단 거리를 BFS로
        # 도달할 수 없으면 -1을 반환
        visited = [[False] * m for _ in range(n)]
        # 행, 열, 이동거리
        queue = deque([(start[0], start[1], 0)])
        visited[start[0]][start[1]] = True

        # 상 하 좌 우
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            row, col, dist = queue.popleft()

            if maps[row][col] == target_char:
                return dist, (row, col)

            for d_row, d_col in directions:
                next_row, next_col = row + d_row, col + d_col

                if not (0 <= next_row < n and 0 <= next_col < m):
                    continue  # 미로 범위 밖 무시
                if visited[next_row][next_col]:
                    continue  # 이미 방문한 칸 무시
                if maps[next_row][next_col] == "X":
                    continue
                    # 벽은 못 지나도록
                visited[next_row][next_col] = True
                queue.append((next_row, next_col, dist + 1))

        return -1, None  # 큐가 빌 때까지 못 찾았으면 도달 불가

    start = find_position("S")

    # 출발지에서 레버까지 최단 거리
    dist_to_lever, lever_pos = bfs(start, "L")
    if dist_to_lever == -1:
        # 레버에 도달 못 하면 애초에 탈출 불가능
        return -1  
        

    # 레버에서 출구까지 최단 거리
    # 레버를 당겨야 문이 열린다/ L을 새 출발점 삼아 다시 BFS
    dist_to_exit, _ = bfs(lever_pos, "E")
    if dist_to_exit == -1:
        return -1  # 레버는 찾았지만 출구로 못 나가면 역시 탈출 불가

    return dist_to_lever + dist_to_exit
