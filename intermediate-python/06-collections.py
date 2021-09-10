# Collections: Counter, namedtuple, OrderedDict, defaultdict, deque

# from collections import Counter

# a = "aaaaabbbbcccc"

# my_counter = Counter(a)
# print(my_counter)
# print(my_counter.items())
# print(my_counter.keys())
# print(my_counter.values())
# print(my_counter.most_common())
# print(my_counter.most_common(2))
# print(my_counter.most_common(2)[0][0])
# print(list(my_counter.elements()))

# from collections import namedtuple

# Point = namedtuple("Point", "x,y")
# pt = Point(1, -4)
# print(pt)
# print(pt.x, pt.y)

# from collections import OrderedDict

# od = OrderedDict()
# # od = {}
# od["a"] = 1
# od["b"] = 2
# od["c"] = 3
# od["d"] = 4
# print(od)

# from collections import defaultdict

# d = defaultdict(int)
# d = defaultdict(float)
# d["b"] = 2.3
# d["a"] = 1.2
# print(d["c"])

from collections import deque

d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)

d.pop()
d.popleft()
print(d)

d.extend([4, 5, 6])
d.extendleft([0, -1, 2])

print(d)

d.rotate()
print(d)
