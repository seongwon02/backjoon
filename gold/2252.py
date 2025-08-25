import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
degree = [0 for _ in range(n+1)]
queue = deque()
answer = []

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    degree[b] += 1

for i in range(1, n+1):
    if degree[i] == 0:
        queue.append(i)

while queue:
    tmp = queue.popleft()
    answer.append(tmp)
    for i in graph[tmp]:
        degree[i] -= 1
        if degree[i] == 0:
            queue.append(i)

print(*answer)