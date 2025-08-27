import sys
from collections import deque
from itertools import combinations
import copy

input = sys.stdin.readline

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

empty = []
virus = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            empty.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def spread(temp_lab):
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if temp_lab[nx][ny] == 0:
                    temp_lab[nx][ny] = 2
                    q.append((nx, ny))

    safe = sum(row.count(0) for row in temp_lab)
    return safe

answer = 0
for walls in combinations(empty, 3):
    temp_lab = copy.deepcopy(lab)
    for x, y in walls:
        temp_lab[x][y] = 1
    answer = max(answer, spread(temp_lab))

print(answer)
