#1676 팩토리얼 0의 개수
import sys 
input = sys.stdin.readline 

def check_zero(n):
    result = 0
    while n > 0:
        if n % 10 != 0:
            break 
        n //= 10
        result += 1
    return result 

num = int(input())
res = 1
for i in range(num, 0, -1):
    res *= i 
    
print(check_zero(res))
