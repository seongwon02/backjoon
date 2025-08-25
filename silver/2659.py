import sys

arr = list(map(int, sys.stdin.readline().rstrip().split()))
num = min(
    arr[0] * 1000 + arr[1] * 100 + arr[2] * 10 + arr[3],
    arr[0] + arr[1] * 1000 + arr[2] * 100 + arr[3] * 10,
    arr[0] * 10 + arr[1] + arr[2] * 1000 + arr[3] * 100,
    arr[0] * 100 + arr[1] * 10 + arr[2] + arr[3] * 1000
)

numSet = set()
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                x = min(
                    i * 1000 + j * 100 + k * 10 + l,
                    i + j * 1000 + k * 100 + l * 10,
                    i * 10 + j + k * 1000 + l * 100,
                    i * 100 + j * 10 + k + l * 1000
                )
                numSet.add(x)

numSet = sorted(list(numSet))
idx = numSet.index(num)
print(idx + 1)

