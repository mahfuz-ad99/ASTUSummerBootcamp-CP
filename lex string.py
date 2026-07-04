import sys
input = sys.stdin.readline

def solve():
    n, m, k = map(int, input().split())
    a = sorted(input().strip())
    b = sorted(input().strip())
    
    i, j = 0, 0
    c = []
    last_type = None  # 'a' or 'b'
    consec = 0
    
    while i < n and j < m:
        # Determine forced choice due to k-limit
        force = None
        if last_type == 'a' and consec == k:
            force = 'b'
        elif last_type == 'b' and consec == k:
            force = 'a'
        
        if force == 'a':
            choice = 'a'
        elif force == 'b':
            choice = 'b'
        else:
            # free choice: pick smaller
            if a[i] <= b[j]:
                choice = 'a'
            else:
                choice = 'b'
        
        if choice == 'a':
            c.append(a[i])
            i += 1
            if last_type == 'a':
                consec += 1
            else:
                last_type = 'a'
                consec = 1
        else:
            c.append(b[j])
            j += 1
            if last_type == 'b':
                consec += 1
            else:
                last_type = 'b'
                consec = 1
    
    print(''.join(c))

t = int(input())
for _ in range(t):
    solve()
