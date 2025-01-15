def f(n):
    r = 0
    for d in str(n):
        r = (r * 10 + int(d)) % 7
    return r

n = input()
print(f(n))
