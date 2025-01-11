n = int(input())
while True:
    n += 1
    if len(str(n)) % 2 == 0 and n >= 1200:
        print(n)
        break