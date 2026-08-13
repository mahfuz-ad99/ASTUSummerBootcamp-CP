import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        gears = [int(x) for x in data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        # If the number of unique elements is less than n, a duplicate exists
        if len(set(gears)) < n:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
