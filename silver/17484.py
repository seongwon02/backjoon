n, m = map(int, input().split())
dp = [[[float("inf"), float("inf"), float("inf")] for _ in range(m)] for _ in range(n+1)]
space = []
for _ in range(n):
    temp = list(map(int, input().split()))
    space.append(temp)

for i in range(m):
    dp[0][i] = [0, 0, 0]

for i in range(1, n+1):
    for j in range(m):
        if j == 0:
            dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + space[i-1][j+1]
            dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + space[i-1][j]
        elif j == m - 1:
            dp[i][j][2] = min(dp[i-1][j-1][1], dp[i-1][j-1][0]) + space[i-1][j-1]
            dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + space[i-1][j]
        else:
            dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + space[i-1][j+1]
            dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + space[i-1][j]
            dp[i][j][2] = min(dp[i-1][j-1][1], dp[i-1][j-1][0]) + space[i-1][j-1]

answer = float("inf")
for i in range(m):
    answer = min(answer, dp[n][i][0], dp[n][i][1], dp[n][i][2])

print(answer)