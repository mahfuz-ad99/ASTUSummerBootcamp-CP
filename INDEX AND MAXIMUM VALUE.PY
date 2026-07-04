import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    res = []
    
    for _ in range(t):
        n, m = int(data[idx]), int(data[idx+1]); idx += 2
        a = [int(data[idx+i]) for i in range(n)]; idx += n
        
        cur_max = max(a)
        
        out = []
        for _ in range(m):
            c = data[idx]; l = int(data[idx+1]); r = int(data[idx+2]); idx += 3
            c = c.decode() if isinstance(c, bytes) else c
            
            if c == '+':
                if l <= cur_max <= r:
                    cur_max += 1
            else:
                if l <= cur_max <= r:
                    cur_max -= 1
            
            out.append(str(cur_max))
        
        res.append(' '.join(out))
    
    sys.stdout.write('\n'.join(res) + '\n')

main()
