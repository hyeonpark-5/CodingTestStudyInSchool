# 17142 연구소 3
from collections import deque 
import sys 
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 바이러스 퍼뜨리기
def bfs(arr):
    q = deque()
    dist = [[-1] * n for _ in range(n)]

    for idx in arr:
        vx, vy = virus_location[idx]
        q.append((vx, vy))
        dist[vx][vy] = 0
    
    max_time = 0
    infected_cnt = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if dist[x][y] >= answer:
                continue

            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
            # 벽이 아니면 갈 수 있음
                if board[nx][ny] != 1:
                    dist[nx][ny] = dist[x][y] + 1 
                    q.append((nx, ny))

                # 빈칸인 경우에만 시간을 갱신하고 카운트
                # 비활성 바이러슨느 지나갈 순 있지만 시간 계산에 포함 안 됨
                    if board[nx][ny] == 0:
                        infected_cnt += 1
                        max_time = dist[nx][ny]
    
    if infected_cnt == empty_cnt:
        return max_time
    else:
        return INF


# 조홥 구하기
def dfs(s, cnt, arr):
    global answer

    if cnt == m:
        res = bfs(arr)
        answer = min(answer, res)
        return 
    
    for i in range(s, len(virus_location)):
        arr.append(i) 
        dfs(i + 1, cnt + 1, arr)
        arr.pop()


n, m = map(int, input().split())
board = []
empty_cnt = 0
virus_location = []

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 0:
            empty_cnt += 1
        elif row[j] == 2:
            virus_location.append((i, j))
    board.append(row)

if empty_cnt == 0:
    print(0)
    sys.exit()


answer = INF
dfs(0, 0, [])
 
if answer == INF:
    print(-1)
else:
    print(answer)