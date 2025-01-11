def s(n):
    return sum(int(c) for c in str(n))

def f(x):
    st = max(1, x - 9 * len(str(x)))
    for n in range(st, x):
        if n + s(n) == x:
            return n
    return -1

x = int(input())
print(f(x))
