import sys
from collections import defaultdict

def solve():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        words = []
        for p in range(3):
            words.append(data[idx:idx+n])
            idx += n
        
        cnt = defaultdict(int)
        for p in range(3):
            for w in words[p]:
                cnt[w] += 1
        
        points = [0, 0, 0]
        for p in range(3):
            for w in words[p]:
                c = cnt[w]
                if c == 1:
                    points[p] += 3
                elif c == 2:
                    points[p] += 1
                # c == 3: 0 points
        
        results.append(f"{points[0]} {points[1]} {points[2]}")
    
    print('\n'.join(results))

solve()
