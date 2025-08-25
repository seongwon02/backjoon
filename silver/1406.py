import sys

right = []
left = list(sys.stdin.readline().rstrip())

n = int(sys.stdin.readline())

for _ in range(n):
    cmd = list(sys.stdin.readline().split())
    
    if cmd[0] == 'L' and left:
        right.append(left.pop())
    if cmd[0] == 'D' and right:
        left.append(right.pop())
    elif cmd[0] == 'B' and left:
        left.pop()
    elif cmd [0] == 'P':
        left.append(cmd[1])
    
print(''.join(left), end="")
while right:
    print(right.pop(), end='')