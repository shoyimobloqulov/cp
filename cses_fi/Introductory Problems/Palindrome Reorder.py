s = input()
f = [0] * 26
for c in s:
    f[ord(c) - ord('A')] += 1
o = 0
m = ""
h = []
for i in range(26):
    c = f[i]
    if c % 2 == 1:
        o += 1
        m = chr(i + ord('A'))
        if o > 1:
            print("NO SOLUTION")
            exit()
    h.append(chr(i + ord('A')) * (c // 2))
h = "".join(h)
print(h + m + h[::-1])
