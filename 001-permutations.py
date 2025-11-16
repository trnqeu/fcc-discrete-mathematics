from itertools import permutations
from math import factorial


perms = {''.join(x) for x in list(permutations("barbarian"))}
print(perms)
print(len(perms))

print(factorial(9))