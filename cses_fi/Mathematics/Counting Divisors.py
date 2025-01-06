m = [0] * 1000005
for i in range(1, 1000005):
    for j in range(i, 1000005, i):
        m[j] += 1
for i in range(int(input())):
    print(m[int(input())])
