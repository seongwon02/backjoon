import sys

n = int(sys.stdin.readline())
board = []

for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    board.append(temp)

dp = [[[0]*3 for _ in range(n)] for _ in range(n)]

dp[0][1][0] = 1

for i in range(n):
    for j in range(2, n): 
        if board[i][j] == 1:
            continue
        
        dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
        if i > 0:
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
        if i > 0 and board[i-1][j] == 0 and board[i][j-1] == 0:
            dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

print(sum(dp[n-1][n-1]))