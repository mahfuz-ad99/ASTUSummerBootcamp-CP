import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    res = []
    
    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = data[idx:idx+n]
        idx += n
        a = [int(x) for x in a]
        
        mn = min(a)
        mx = max(a)
        d = mx - mn
        ans = (d + 1) // 2
        res.append(str(ans))
    
    print('\n'.join(res))

main()
