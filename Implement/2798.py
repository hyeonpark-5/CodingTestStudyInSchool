def dfs(x, s, cnt):
    global answer
    
    if x == 3:
        if cnt <= m:
            answer = (max(answer, cnt))
            return 
    
    if cnt > m:
        return
        
    for i in range(s, n):
        dfs(x + 1, i + 1, cnt + arr[i])


n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
dfs(0, 0, 0)

print(answer)