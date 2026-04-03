# 4485 녹색 옷 입은 애가 젤다지?
import heapq
import sys

input = sys.stdin.readline
INF = float('inf')
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 1

def dijstra(n, board):

    # distance 초기화
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = board[0][0]

    # heapq 초기화
    pq = []
    # 시작점에서도 돈을 뺐길 수 있으므로 board[0][0]이어야됨.
    heapq.heappush(pq, (board[0][0], 0, 0))

    # q 돌기
    while pq:
        d, x, y = heapq.heappop(pq)

        if distance[x][y] < d:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                cost = d + board[nx][ny]

                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost 
                    heapq.heappush(pq, (cost, nx, ny))


    print(f'Problem {count}: {distance[n - 1][n - 1]}')

        
while True:
    n = int(input())
    if n == 0:
        break 
    board = [list(map(int, input().split())) for _ in range(n)]
    dijstra(n, board)
    count += 1