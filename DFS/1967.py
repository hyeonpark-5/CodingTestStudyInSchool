# 1967 트리의 지름
import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, summ):
    for i, v in tree[x]:
        if check[i] == -1:
            check[i] = summ + v
            dfs(i, summ + v)            


n = int(input())
answer = -2147000000
tree = [[] for _ in range(n + 1)]


for _ in range(n - 1):
    x, y, v = map(int, input().split())
    tree[x].append((y, v))
    tree[y].append((x, v))

check = [-1] * (n + 1)
check[1] = 0
dfs(1, 0)

start = check.index(max(check))

check = [-1] * (n + 1)
check[start] = 0
dfs(start, 0)

print(max(check))