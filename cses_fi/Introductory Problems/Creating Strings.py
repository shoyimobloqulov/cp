from itertools import permutations
 
s = input()
p = sorted(set("".join(x) for x in permutations(s)))
print(len(p))
print("\n".join(p))
