n = int(input())

answer = 0
for i in range(n):
    res = 0
    res += i 
    s = str(res)
    for j in s:
        res += int(j)
    if res == n:
        answer = i
        break

print(answer)