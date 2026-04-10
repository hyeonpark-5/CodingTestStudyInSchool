# 14940 쉬운 최단 거리
from collections import deque 
import sys 
input = sys.stdin.readline 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

start_x = 0
start_y = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            start_x = i 
            start_y = j
        
        if board[i][j] == 0:
            visited[i][j] = 0

q = deque()
q.append((start_x, start_y))

visited[start_x][start_y] = 0

while q:
    x, y = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

for i in range(n):
    for j in range(m):      
        print(visited[i][j], end = " ")
    print()
