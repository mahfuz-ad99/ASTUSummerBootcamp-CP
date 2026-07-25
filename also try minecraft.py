def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    # prefix_down[i] = sum of max(0, a[k]-a[k+1]) for k in 0..i-1 (moving left->right)
    # prefix_up[i]   = sum of max(0, a[k+1]-a[k]) for k in 0..i-1 (moving right->left)
    prefix_down = [0] * n
    prefix_up = [0] * n
    for i in range(n - 1):
        diff = a[i] - a[i + 1]
        prefix_down[i + 1] = prefix_down[i] + (diff if diff > 0 else 0)
        prefix_up[i + 1] = prefix_up[i] + (-diff if diff < 0 else 0)

    out = []
    for _ in range(m):
        s, t = map(int, input().split())
        s -= 1
        t -= 1
        if s < t:
            res = prefix_down[t] - prefix_down[s]
        else:
            res = prefix_up[s] - prefix_up[t]
        out.append(str(res))

    print('\n'.join(out))

main()
