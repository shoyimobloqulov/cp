import math

x, y = map(int, input().split())

z = math.log(abs((x + y)**2 + math.sqrt(abs(y) + 2) - ((x - (x * y) / (x**2 / 2 - 5))))) + (math.cos(x + y)**2) / ((x + y)**(1/3))

print(f"{z:.2f}")
