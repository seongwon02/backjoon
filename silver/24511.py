from collections import deque
import sys

n = int(sys.stdin.readline())
qs = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

dq = deque()

for i in range(n):
    if qs[i] == 0:
        dq.append(arr[i])

for j in range(m):
    dq.appendleft(num[j])
    print(dq.pop(), end=" ")