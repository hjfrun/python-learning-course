# Sets: unordered, mutable, no duplicates

# myset = {1, 2, 3, 2, 1}
# print(myset)

# myset = set([1, 2, 3, 2])
# print(myset)

# myset = set()
# print(type(myset))

# myset = set()
# myset.add(1)
# myset.add(2)
# myset.add(3)

# myset.remove(4)
# myset.discard(3)
# myset.discard(4)
# myset.clear()
# print(myset)

# for x in myset:
#     print(x)

# if 1 in myset:
#     print("yes")


from typing import FrozenSet


odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}
# u = odds.union(evens)
# print(u)

# i = odds.intersection(primes)
# print(i)

# i = evens.intersection(primes)
# print(i)

# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setB = {1, 2, 3, 10, 11, 12}

# diff = setA.difference(setB)
# diff = setB.difference(setA)
# diff = setA.symmetric_difference(setB)
# print(diff)

# setA.update(setB)
# print(setA)

# setA.intersection_update(setB)
# setA.difference_update(setB)
# print(setA)

# setA = {1, 2, 3, 4, 5, 6}
# setB = {1, 2, 3}
# setC = {7, 8}

# print(setA.issuperset(setB))
# print(setA.isdisjoint(setC))

# setA = {1, 2, 3, 4, 5, 6}
# setB = setA
# setB = setA.copy()
# setB.add(7)

# print(setA)
# print(setB)

a = frozenset([1, 2, 3, 4])

# a.add(5)
print(a)
