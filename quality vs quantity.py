import sys
input = sys.stdin.readline

t = int(input())
res = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    
    # prefix sum from smallest (ascending)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + a[i]
    
    total = prefix[n]
    
    found = False
    max_k = (n - 1) // 2  # need k + (k+1) <= n
    for k in range(1, max_k + 1):
        top_k_sum = total - prefix[n - k]      # sum of largest k elements
        bottom_k1_sum = prefix[k + 1]          # sum of smallest k+1 elements
        if top_k_sum > bottom_k1_sum:
            found = True
            break
    
    res.append("YES" if found else "NO")

print("\n".join(res))
