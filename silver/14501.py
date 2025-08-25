import sys

n = int(sys.stdin.readline())
arr = []
dp = [0] * n

for _ in range(n):
    t, p = map(int, sys.stdin.readline().rstrip().split())
    arr.append([t, p])

for i in range(n):
    t, p = arr[i]
    
    if i > 0:
        dp[i] = max(dp[i], dp[i-1])
    
    if i + t <= n:
        dp[i + t - 1] = max(dp[i + t - 1], dp[i-1] + p)
    
print(max(dp))