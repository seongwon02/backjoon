import sys

n = int(sys.stdin.readline())
x = sys.stdin.readline().rstrip()

num = []
op = []
answer = float("-inf")

for i in range(n):
    if i % 2 == 0:
        num.append(int(x[i]))
    else:
        op.append(x[i])

def calc(a, op, b):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b

def dfs(idx, value):
    global answer
    
    if idx == len(op):
        answer = max(value, answer)
        return

    next_val = calc(value, op[idx], num[idx+1])
    dfs(idx + 1, next_val)
    
    if idx + 1 < len(op):
        temp = calc(num[idx+1], op[idx+1], num[idx+2])
        next_val = calc(value, op[idx], temp)
        dfs(idx+2, next_val)
        
dfs(0, num[0])
print(answer)