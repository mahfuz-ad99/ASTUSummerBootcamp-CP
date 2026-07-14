import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    res = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n

        ones_pos = [i for i, v in enumerate(a) if v == 1]
        m = len(ones_pos)
        if m == 0:
            res.append(0)
            continue

        total_zeros = n - m
        pz = [0] * (n + 1)  # prefix zero counts
        for i in range(n):
            pz[i+1] = pz[i] + (1 - a[i])

        zeros_after = [total_zeros - pz[o+1] for o in ones_pos]

        lo, hi, found = 0, m - 1, -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if zeros_after[mid] <= mid:
                found = mid
                hi = mid - 1
            else:
                lo = mid + 1

        res.append(found if found != -1 else m)

    print('\n'.join(map(str, res)))

main()
