import sys
from collections import deque

n, m, h = map(int, sys.stdin.readline().split())
boxes = []
matrix = [[[float("inf") for _ in range(n)] for _ in range(m)] for _ in range(h)]
queue = deque()
movement = [[1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]]

for k in range(h):
    tomatos = []
    for i in range(m):
        tmp = list(map(int, sys.stdin.readline().split()))
        
        for j in range(n):
            if tmp[j] == -1:
                matrix[k][i][j] = -1
            elif tmp[j] == 1:
                queue.append((k, i, j, 0))
                matrix[k][i][j] = 0

        tomatos.append(tmp)
    boxes.append(tomatos)

while queue:
    w, x, y, day = queue.popleft()
    
    for i in range(6):
        dx = x + movement[0][i]
        dy = y + movement[1][i]
        dh = w + movement[2][i]
        
        if dx > -1 and dx < m and \
            dy > -1 and dy < n and \
            dh > -1 and dh < h and \
            matrix[dh][dx][dy] != -1 and \
            day + 1 < matrix[dh][dx][dy]:
            
            matrix[dh][dx][dy] = day + 1
            queue.append((dh, dx, dy, day + 1))

success = True
answer = 0

for k in range(h):
    for i in range(m):
        for j in range(n):
            if matrix[k][i][j] == float("inf"):     
                success = False
            
            answer = max(answer, matrix[k][i][j])

if success:
    print(answer)
else:
    print(-1)