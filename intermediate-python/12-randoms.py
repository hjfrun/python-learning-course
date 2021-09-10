import random

# a = random.random()
# a = random.uniform(1, 10)
# a = random.randint(1, 10) ## contain 10
# a = random.randrange(1, 10) ## exclude 10
# a = random.normalvariate(0, 1)
# print(a)

# mylist = list("ABCDEFGH")
# a = random.choice(mylist)
# a = random.sample(mylist, 3)
# a = random.choices(mylist, k=5)
# print(a)

# random.shuffle(mylist)
# print(mylist)

# random.seed(1)
# print(random.random())
# print(random.randint(1, 10))

# random.seed(2)
# print(random.random())
# print(random.randint(1, 10))

# random.seed(1)
# print(random.random())
# print(random.randint(1, 10))

# random.seed(2)
# print(random.random())
# print(random.randint(1, 10))


# import secrets

# a = secrets.randbelow(10)
# binary 1111
# a = secrets.randbits(4)

# mylist = list("ABCDEFGH")
# a = secrets.choice(mylist)
# print(a)

import numpy as np

# a = np.random.randint(0, 10, (3, 4))
"""
a = np.random.randint(0, 10, (3, 4))
[[7 3 5 2]
 [4 3 6 9]
 [3 1 0 4]]
"""
# print(a)
# a = np.random.rand(3)
# [0.46584092 0.00158835 0.86275728]
"""
a = np.random.rand(3, 3)

[[0.76068049 0.67262335 0.05971037]
 [0.50225049 0.53966931 0.49108122]
 [0.97006236 0.44139675 0.28126239]]
"""


# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr)
# np.random.shuffle(arr)
# print(arr)

np.random.seed(1)
print(np.random.rand(3, 3))

# np.random.seed(1)
print(np.random.rand(3, 3))
