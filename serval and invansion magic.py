import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    diff = [i for i in range(n//2) if s[i] != s[n-1-i]]
    if not diff:
        print("Yes")
    else:
        l, r = min(diff), max(diff)
        ok = all(s[i] != s[n-1-i] for i in range(l, r+1))
        print("Yes" if ok else "No")
