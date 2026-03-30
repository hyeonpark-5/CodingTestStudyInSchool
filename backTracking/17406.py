# 17406 배열 돌리기 4
import sys 
input = sys.stdin.readline

def rotate(idx, matrix):
    r, c, s = check[idx]
    r, c = r - 1, c - 1
    for i in range(1, s + 1):
        r1, c1, r2, c2 = r - i, c - i, r + i, c + i

        temp = matrix[r1][c1]

        for k in range(r1, r2):
            matrix[k][c1] = matrix[k + 1][c1]
        
        for k in range(c1, c2):
            matrix[r2][k] = matrix[r2][k + 1]
        
        for k in range(r2, r1, -1):
            matrix[k][c2] = matrix[k - 1][c2]

        for k in range(c2, c1, -1):
            matrix[r1][k] = matrix[r1][k - 1]
        
        matrix[r1][c1 + 1] = temp 


def dfs(x, arr):
    global answer
    if x == k:
        matrix = [row[:] for row in board]
        for a in arr:
            rotate(a, matrix)
        
        for m in matrix:
            answer = min(answer, sum(m))


    for i in range(k):
        if visited[i] == 0:
            visited[i] = 1
            dfs(x + 1, arr + [i])
            visited[i] = 0




n, m, k = map(int, input().split())

answer = 2147000000
board = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * k
check = []

for _ in range(k):
    r, c, s = map(int, input().split())
    check.append((r, c, s))

dfs(0, [])
print(answer)

