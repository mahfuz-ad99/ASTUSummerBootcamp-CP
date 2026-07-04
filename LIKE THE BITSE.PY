import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    res = []
    
    for _ in range(t):
        n, k = int(data[idx]), int(data[idx+1]); idx += 2
        s = data[idx].decode(); idx += 1
        
        # Check feasibility: no window of length k can have all 1s
        # (if all k in a window are 1, the max in that window must not be at any of them, impossible)
        ok = True
        if k <= n:
            cnt = 0
            for i in range(n):
                if s[i] == '1':
                    cnt += 1
                else:
                    cnt = 0
                if i >= k - 1:
                    if cnt >= k:
                        ok = False
                        break
        
        if not ok:
            res.append("NO")
            continue
        
   
        
        p = [0] * n
        zeros_positions = [i for i in range(n) if s[i] == '0']
        ones_positions = [i for i in range(n) if s[i] == '1']
        
        num_zeros = len(zeros_positions)
        num_ones = len(ones_positions)
        
        # zeros get the largest values n, n-1, ..., in order of position
        val = n
        for i in zeros_positions:
            p[i] = val
            val -= 1
        # ones get smallest values 1,2,... in order of position
        val = 1
        for i in ones_positions:
            p[i] = val
            val += 1
        
        res.append("YES")
        res.append(' '.join(map(str, p)))
    
    print('\n'.join(res))

main()
