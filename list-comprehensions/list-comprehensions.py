# [ expr for val in collection ]
# [ expr for val in collection if <test> ]
# [ expr for val in collection if <test1> and <test2> ]
# [ expr for val1 in collection1 for val2 in collection2 ]

# comb = [a + b for a in "life" for b in "study"]
# print(comb)

# squares = []
# for i in range(1, 101):
#     squares.append(i ** 2)

# print(squares)

# squares = [i ** 2 for i in range(1, 101)]
# print(squares)

# remainders5 = [x ** 2 % 5 for x in range(1, 101)]
# print(remainders5)

# remainder11 = [x ** 2 % 11 for x in range(1, 101)]
# print(remainder11)

# movies = ["Hello", "World", "Jaidk", "Helloslsoe", "Hero"]
# h_movies = [title for title in movies if title.startswith("H")]
# print(h_movies)

# v = [2, -3, 1]
# print(v * 4)
# l = [2, 4, 6] + [1, 3]
# print(l)

# v4 = [x * 4 for x in v]
# print(v4)

# A = [1, 3, 5, 7]
# B = [2, 4, 6, 8]

# cp = [(a, b) for a in A for b in B]
# print(cp)

# extract information
users = [
    {"name": "hjf", "age": 31},
    {"name": "htj", "age": 2},
    {"name": "wlz", "age": 56},
]

# usernames = [user["name"] for user in users]
# print(usernames)

usernames = [user["name"] for user in users if user["age"] < 10]
print(usernames)
