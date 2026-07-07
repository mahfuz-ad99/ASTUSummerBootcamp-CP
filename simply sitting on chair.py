import sys
input = sys.stdin.readline

t = int(input())
res = []
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n+1):
        if p[i-1] <= i:
            count += 1
    res.append(str(count))
print('\n'.join(res))
