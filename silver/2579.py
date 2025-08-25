import sys

n = int(sys.stdin.readline())
stairs = []
dp = [[0, 0] for _ in range(n)]

for i in range(n):
    s = int(sys.stdin.readline())
    stairs.append(s)

dp[0][0] = stairs[0]

if n >= 2:
    dp[1][0] = stairs[1]
    dp[1][1] = stairs[0] + stairs[1]

for i in range(2, n):
    dp[i][0] = max(dp[i - 2][0] + stairs[i] ,dp[i - 2][1] + stairs[i])
    dp[i][1] = dp[i - 1][0] + stairs[i]

print(max(dp[-1]))