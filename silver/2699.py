import sys

matrix = [[False for _ in range(101)] for _ in range(101)]
answer = 0

for _ in range(4):
    a, b, c, d = map(int, sys.stdin.readline().split())
    
    for i in range(a, c):
        for j in range(b, d):
            if not matrix[i][j]:
                answer += 1
                matrix[i][j] = True
    
print(answer)