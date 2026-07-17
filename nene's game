def solve():
    k, q = map(int, input().split())
    a = list(map(int, input().split()))
    ns = list(map(int, input().split()))
    
    results = []
    for n in ns:
        m = n
        while True:
            kicked = 0
            for x in a:
                if x <= m:
                    kicked += 1
                else:
                    break
            if kicked == 0:
                break
            m -= kicked
        results.append(m)
    
    print(*results)

t = int(input())
for _ in range(t):
    solve()
