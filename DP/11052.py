n = int(input())
cards = list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(i , n + 1):
        if i == j:
            dp[j] = max(dp[j], cards[i - 1])
        else:
            dp[j] = max(dp[j], dp[j - i] + dp[i])

print(dp[n])