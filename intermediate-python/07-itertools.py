# Itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

# from itertools import product

# a = [1, 2]
# b = [3, 4]

# prod = product(a, b, repeat=2)
# print(list(prod))

# from itertools import permutations

# a = [1, 2, 3]
# perm = permutations(a, 2)
# print(list(perm))

# from itertools import combinations, combinations_with_replacement

# a = [1, 2, 3, 4]
# comb = combinations(a, 2)
# print(list(comb))

# comb_wr = combinations_with_replacement(a, 2)
# print(list(comb_wr))

# from itertools import accumulate
# import operator

# a = [1, 2, 5, 3, 4]
# acc = accumulate(a, func=max)
# # acc = accumulate(a, func=operator.mul)
# print(list(acc))

# from itertools import groupby


# def small_than_3(x):
#     return x < 3


# a = [1, 2, 3, 4]
# # groupby_obj = groupby(a, key=small_than_3)
# groupby_obj = groupby(a, key=lambda x: x < 3)
# # print(groupby_obj)
# for key, value in groupby_obj:
#     print(key, list(value))

# persons = [
#     {"name": "Tim", "age": 25},
#     {"name": "Dan", "age": 25},
#     {"name": "Lisa", "age": 27},
#     {"name": "Claire", "age": 28},
# ]

# group_obj = groupby(persons, key=lambda x: x["age"])

# for key, value in group_obj:
#     print(key, list(value))

from itertools import count, cycle, repeat

# a = [1, 2, 3]
# for i in cycle(a):
#     print(i)

for i in repeat(1, 4):
    print(i)
