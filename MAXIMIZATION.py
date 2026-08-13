import sys
from collections import Counter

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    t = int(input_data[idx]); idx += 1
    results = []
    for _ in range(t):
        n = int(input_data[idx]); idx += 1
        a = [int(input_data[idx + i]) for i in range(n)]
        idx += n
        
        cnt = Counter(a)
        b = []
        
        # place 0,1,2,... as long as available (one copy each)
        x = 0
        while cnt[x] > 0:
            b.append(x)
            cnt[x] -= 1
            x += 1
        
        # append remaining elements
        for val, c in cnt.items():
            for _ in range(c):
                b.append(val)
        
        results.append(' '.join(map(str, b)))
    
    print('\n'.join(results))

solve()
