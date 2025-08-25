import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = []

answer = [0] * n
stack.append((arr[0], 1))

for i in range(1, n):    
    while stack:
        num, idx = stack.pop()
        
        if num > arr[i]:
            answer[i] = idx
            stack.append((num, idx))
            break
    

    stack.append((arr[i], i+1))
    
        
print(*answer)