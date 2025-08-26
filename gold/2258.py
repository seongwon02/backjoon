import sys

n, m = map(int, sys.stdin.readline().split())
meat = {}
answer = float("inf")

for i in range(n):
    weight, price = map(int, sys.stdin.readline().split())
    
    if price in meat:
        meat[price].append(weight)
    else:
        meat[price] = [weight]

meatKeys = sorted(meat.keys())
totalW = 0

for price in meatKeys:
    weights = sorted(meat[price])
    i = 0
    
    while weights:
        totalW += weights.pop()
        i += 1
        if totalW >= m:
            answer = min(answer, price * i)
    
    i = 0

if answer == float("inf"):
    print(-1)
else:
    print(answer)