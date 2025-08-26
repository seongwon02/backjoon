import sys

n, m = map(int, sys.stdin.readline().split())
subjects = []

for _ in range(n):
    p, l = map(int, sys.stdin.readline().split())
    tmp = list(map(int, sys.stdin.readline().split()))
    tmp.sort()
    
    if p < l:
        subjects.append(1)
    else:
        subjects.append(tmp[p-l])

subjects.sort()

while sum(subjects) > m:
    subjects.pop()

print(len(subjects))   
