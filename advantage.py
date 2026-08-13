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
        idx += 1
        s = [int(x) for x in data[idx : idx + n]]
        idx += n
        
        # Find max1 and max2
        sorted_s = sorted(s, reverse=True)
        max1 = sorted_s[0]
        max2 = sorted_s[1]
        
        res = []
        for val in s:
            if val == max1:
                res.append(str(val - max2))
            else:
                res.append(str(val - max1))
        
        out.append(" ".join(res))
        
    print("\n".join(out))

if __name__ == '__main__':
    solve()
