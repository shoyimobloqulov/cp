x,y = map(int,input().split())
a,b = x,y
if x > y:
    y = (a + b) / 2
    x = 4 * a * b
else:
    x = (a + b) / 2
    y = 4 * a * b
print(f"{x:.1f} {y:.1f}")