import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        a = [int(x) for x in data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        a.sort()
        max_beauty = a[-1] + a[-2] - a[0] - a[1]
        out.append(str(max_beauty))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
