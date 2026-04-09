# 15683 감시
import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 상우하좌
dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]
cctv_idx = {1: [(1,), (2,), (3,), (4,)],
            2: [(1, 3), (2, 4)], 
            3:[(1, 2), (2, 3), (3, 4), (4, 1)], 
            4: [(1, 2, 3), (2, 3, 4), (3, 4, 1), (4, 1, 2)], 
            5: [(1, 2, 3, 4)]}

# v는 cctv_location에서 몇번째 cctv인가
def dfs(v, current_board):
    global answer
    if v == len(cctv_location):
        cnt = 0
        for i in range(n):
            for j in range(m):
                if current_board[i][j] == 0:
                    cnt += 1 
        answer = min(answer, cnt)
        return 

    # cctv의 위치
    x, y = cctv_location[v]
    # cctv의 종류
    cctv_type = board[x][y]

    for directions in cctv_idx[cctv_type]:
        temp_board = [row[:] for row in current_board]
        for i in directions:
            nx = x
            ny = y
            while True:
                nx += dx[i]
                ny += dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if temp_board[nx][ny] == 6:
                        break
                    if temp_board[nx][ny] == 0:
                        temp_board[nx][ny] = '#'
                else:
                    break
        dfs(v + 1, temp_board)
                
# n: 세로, m: 가로
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cctv_location = []
answer = 2147000000


for i in range(n):
    for j in range(m):
        if 0 < board[i][j] and board[i][j] < 6:
            cctv_location.append((i, j))

dfs(0, board)
print(answer)