import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    t = int(data[0])
    results = []
    
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        s = data[idx+1]
        idx += 2
        
        target_char = s[-1]
        # Count how many characters are NOT equal to the last character
        ans = sum(1 for char in s if char != target_char)
        results.append(str(ans))
        
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
