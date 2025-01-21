from collections import Counter
def solve(n): 
    s_san = Counter(n) 
    max_s = max(s_san.values()) 
    m = [s for s, s_t in s_san.items() if s_t == max_s] 
    return min(m)

n = int(input())
l = list(map(int,input().split()))
print(solve(l))