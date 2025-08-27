import sys
input = sys.stdin.readline

n = int(input())
answer = 0

cols = [False for _ in range(n)]   
diag1 = [False for _ in range(n*2)]
diag2 = [False for _ in range(n*2)]

def dfs(row):
    global answer
    if row == n:
        answer += 1
        return
    
    for col in range(n):
        if cols[col] or diag1[row+col] or diag2[row-col+n]:
            continue
        
        cols[col] = diag1[row+col] = diag2[row-col+n] = True
        dfs(row+1)
        cols[col] = diag1[row+col] = diag2[row-col+n] = False

dfs(0)
print(answer)
