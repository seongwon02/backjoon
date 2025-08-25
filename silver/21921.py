import sys

n, x = map(int, sys.stdin.readline().split())
visitors = list(map(int, sys.stdin.readline().split()))

if max(visitors):
    visitedCnt = sum(visitors[:x])
    preVisitedCnt = visitedCnt
    period = 1
    
    for i in range(x, len(visitors)):
        curVisitedCnt = preVisitedCnt - visitors[i - x] + visitors[i]

        if visitedCnt == curVisitedCnt:
            period += 1
        elif visitedCnt < curVisitedCnt:
            visitedCnt = curVisitedCnt
            period = 1
        
        preVisitedCnt = curVisitedCnt
    
    print(visitedCnt)
    print(period)
else:
    print("SAD")