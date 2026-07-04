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
        
        # dp represented as a bitmask. Bit 0 is set to 1 initially (0 points reachable).
        dp = 1 
        
        for _ in range(n):
            num_subtasks = int(data[idx])
            idx += 1
            
            step_size = 100 // num_subtasks
            
            # Combine all possible score shifts from this problem
            next_dp = dp
            for x in range(1, num_subtasks + 1):
                next_dp |= (dp << (x * step_size))
                
            dp = next_dp
            
        # The target mask requires every bit from 0 to 100*n to be 1.
        # (1 << (100 * n + 1)) - 1 creates a binary number with 100*n + 1 ones.
        target_mask = (1 << (100 * n + 1)) - 1
        
        # Mask out any bits higher than 100*n just in case, then compare
        if (dp & target_mask) == target_mask:
            out.append("Yes")
        else:
            out.append("No")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
