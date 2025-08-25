import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
queue = deque()
target = [-1, -1]
matrix = []
answer = [[float("inf") for _ in range(m)] for _ in range(n)]
movement = [[1,-1,0,0], [0,0,1,-1]]

for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    
    for j in range(m):
        if tmp[j] == 2:
            target[0] = i
            target[1] = j
        elif tmp[j] == 0:
            answer[i][j] = 0
    
    matrix.append(tmp)

queue.append((target[0], target[1], 0))
answer[target[0]][target[1]] = 0

while queue:
    x, y, cnt = queue.popleft()
    
    for i in range(4):
        dx = x + movement[0][i]
        dy = y + movement[1][i]
        
        if dx > -1 and dx < n and \
            dy > -1 and dy < m and \
            matrix[dx][dy] == 1:
                if cnt + 1 < answer[dx][dy]:
                    answer[dx][dy] = cnt + 1
                    queue.append((dx, dy, cnt + 1))
                    
for i in range(n):
    for j in range(m):
        if answer[i][j] == float("inf"):
            answer[i][j] = -1
    print(*answer[i])
                    