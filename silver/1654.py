import sys

k, n = map(int, sys.stdin.readline().split())
cables = []

for _ in range(k):
    cables.append(int(sys.stdin.readline()))

left = 1
right = max(cables)
length = (left + right) // 2

while True:
    if left > right:
        break
        
    total = 0
    
    for i in range(k):
        total += cables[i] // length
    
    if total < n:
        right = length - 1
    else:
        left = length + 1
    
    length = (left + right) // 2  
    
print(length)   