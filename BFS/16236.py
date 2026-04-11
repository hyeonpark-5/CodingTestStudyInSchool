#16236 아기 상어 (bfs)
from collections import deque 
import sys 
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline 

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 물고기와의 거리계산
def bfs(start_x, start_y, shark_size):
    visited = [[-1] * n for _ in range(n)]
    eat_fish = []
    q = deque()
    q.append((start_x, start_y))

    visited[start_x][start_y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1 and board[nx][ny] <= shark_size:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                
                if 0 < board[nx][ny] < shark_size:
                    eat_fish.append((visited[nx][ny], nx, ny))

    eat_fish.sort(key=lambda x:(x[0], x[1], x[2]))  
    return eat_fish 
        


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
shark_size = 2
shark_eat = 0


shark_x = 0
shark_y = 0

answer = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            shark_x = i
            shark_y = j
            board[i][j] = 0

while True:
    eat_list = bfs(shark_x, shark_y, shark_size)

    if not eat_list:
        break

    dist, nx, ny = eat_list[0]

    answer += dist

    shark_x = nx 
    shark_y = ny 
    board[nx][ny] = 0

    shark_eat += 1
    if shark_eat == shark_size:
        shark_size += 1
        shark_eat = 0

print(answer)