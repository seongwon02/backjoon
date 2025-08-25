import sys

arr = list(sys.stdin.readline().rstrip())

answer = 0
stack = []
stack.append(arr[0])

for i in range(1, len(arr)):
    x = arr[i]
    preX = arr[i-1]
    
    if x == '(':
        stack.append(x)
    else:
        stack.pop()
        if preX == '(':
            answer += len(stack)
        else:
            answer += 1

print(answer)