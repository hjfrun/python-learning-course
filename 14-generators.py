# def mygenerator():
#     yield 10
#     yield 2
#     yield 3


# g = mygenerator()
# print(g)

# for i in g:
#     print(i)

# print(next(g))
# print(next(g))
# print(next(g))

# print(sum(g))
# print(sorted(g))


# def countdown(num):
#     print("Starting...")
#     while num > 0:
#         yield num
#         num -= 1


# cd = countdown(4)
# value = next(cd)
# print(value)

# print(next(cd))
# print(next(cd))
# print(next(cd))


# def firstN(n):
#     nums = []
#     num = 0
#     while num < n:
#         nums.append(num)
#         num += 1
#     return nums

# print(firstN(10))
# print(sum(firstN(10)))

# import sys


# def firstN_g(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1


# print(sum(firstN_g(10)))
# print(sys.getsizeof(firstN_g(10)))


# def fibonacci(limit):
#     # 0 1 1 2 3 5 8 13 21 ...
#     a, b = 0, 1
#     while a < limit:
#         yield a
#         a, b = b, a + b


# fib = fibonacci(300)
# for i in fib:
#     print(i)

import sys

my_g = (i for i in range(30) if i % 2 == 0)
print(list(my_g))
# for i in my_g:
#     print(i)

my_list = [i for i in range(30) if i % 2 == 0]
print(my_list)

print(sys.getsizeof(my_g))
print(sys.getsizeof(my_list))
