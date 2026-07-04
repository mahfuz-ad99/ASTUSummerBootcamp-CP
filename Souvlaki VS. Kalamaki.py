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
        a = [int(x) for x in data[idx + 1 : idx + 1 + n]]
        idx += 1 + n
        
        # Sort the array to check the required adjacent equality
        a.sort()
        
        possible = True
        # In 0-indexed terms, 1-based even rounds i = 2, 4, 6... 
        # correspond to 0-indexed positions i-1 = 1, 3, 5...
        for i in range(1, n - 1, 2):
            if a[i] != a[i + 1]:
                possible = False
                break
                
        if possible:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
