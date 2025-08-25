from collections import deque
import sys

n = int(sys.stdin.readline())
matrix = [[False for _ in range(n+1)] for _ in range(n+1)]
answer = []

while True:
    a, b = map(int, sys.stdin.readline().split())
    
    if a == -1 and b == -1:
        break
    
    matrix[a][b] = True
    matrix[b][a] = True

def calc(num):
    queue = deque()
    friends = [float("inf")] * (n + 1)
    friends[0] = 0
    queue.append((num, 0))
    friends[num] = 0
    
    while queue:
        cur, score = queue.popleft()
        
        for i in range(1, n+1):
            if matrix[cur][i] and score + 1 <= friends[i]:
                friends[i] = score + 1
                queue.append((i, score + 1))
    
    return max(friends)

scoreList = [calc(i) for i in range(1, n+1)]
score = min(scoreList)

for i in range(n):
    if scoreList[i] == score:
        answer.append(i + 1)

print(score, len(answer))
print(*answer)