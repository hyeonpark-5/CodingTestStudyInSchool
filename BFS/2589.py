# 2589 보물섬
# 2589 보물섬
from collections import deque 
import sys 
input = sys.stdin.readline 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(s, e):
    check = [[-1] * m for _ in range(n)]
    maxx = -2147000000

    q = deque()
    q.append((s, e))

    check[s][e] = 0

    while q:
        x, y = q.popleft()

        maxx = max(maxx, check[x][y])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] != 'W' and check[nx][ny] == -1:
                    check[nx][ny] = check[x][y] + 1
                    q.append((nx, ny))

    return maxx

n, m = map(int, input().split())
board = [list(map(str, input().rstrip())) for _ in range(n)]
answer = -2147000000

for i in range(n):
    for j in range(m):
        if board[i][j] == "L":
            res = bfs(i, j)
            answer = max(answer, res)

print(answer)
