import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        prefix_sum = 0
        best = None
        res = []
        for j in range(1, n+1):
            prefix_sum += a[j-1]
            cur = prefix_sum // j
            if best is None or cur < best:
                best = cur
            res.append(best)
        
        out.append(' '.join(map(str, res)))
    
    sys.stdout.write('\n'.join(out) + '\n')

main()
