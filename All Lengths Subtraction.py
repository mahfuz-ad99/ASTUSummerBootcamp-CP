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
        p = [int(x) for x in data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        # Find the index of each number from 1 to n
        pos = {val: i for i, val in enumerate(p)}
        
        left = 0
        right = n - 1
        possible = True
        
        for v in range(1, n + 1):
            target_idx = pos[v]
            if target_idx == left:
                left += 1
            elif target_idx == right:
                right -= 1
            else:
                possible = False
                break
                
        if possible:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
