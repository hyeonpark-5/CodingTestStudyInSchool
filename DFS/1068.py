#1068 트리
import sys 
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x):
    global cnt

    is_leaf = True
    for i in graph[x]:
        if i == erase:
            continue

        is_leaf = False 
        dfs(i)
    
    if is_leaf:
        cnt += 1

n = int(input())
board = list(map(int, input().split()))
erase = int(input())
root_idx = -1
cnt = 0
graph = [[] for _ in range(n)]

for i in range(n):
    if board[i] == -1:
        root_idx = i
    else:
        graph[board[i]].append(i)

if erase == root_idx:
    print(0)
else:
    dfs(root_idx)
    print(cnt)