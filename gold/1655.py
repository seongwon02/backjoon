import heapq
import sys

n = int(sys.stdin.readline())

leftHeap = []
rightHeap = []
answer = []

for i in range(n):
    num = int(sys.stdin.readline())
    
    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, (-num, num))
    else:
        heapq.heappush(rightHeap, (num, num))
    
    if rightHeap and leftHeap[0][1] > rightHeap[0][0]:
        s = heapq.heappop(rightHeap)[0]
        l = heapq.heappop(leftHeap)[1]
        
        heapq.heappush(leftHeap, (-s, s))
        heapq.heappush(rightHeap, (l, l))
    
    answer.append(leftHeap[0][1])

for i in answer:
    print(i)