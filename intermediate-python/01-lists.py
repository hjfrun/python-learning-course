# Lists: ordered, mutable, allows duplicate elements


# mylist = ["banana", "cherry", "apple"]
# print(mylist)

# item = mylist[-1]
# print(item)

# mylist2 = [5, True, "aple", 1322]
# print(mylist2)

# for i in mylist:
#     print(i)

# if "apple" in mylist:
#     print("yes")
# else:
#     print("no")

# print(len(mylist))
# mylist.append('lemon')
# print(mylist)

# mylist.insert(1, "blueberry")
# print(mylist)

# item = mylist.pop()
# print(item)
# print(mylist)

# item = mylist.remove('cherry')
# print(item)

# mylist.clear()
# new_list = sorted(mylist)
# print(new_list)
# print(mylist)


# mylist = [0] * 5
# print(mylist)

# mylist2 = [1,2,3,4,5]
# new_list = mylist + mylist2
# print(new_list)

# mylist = [1,2,3,4,5,6,7,8,9]
# a = mylist[::-1]
# print(a)

# list_org = ["banana", "cherry", "apple"]

# list_cpy = list_org.copy()
# list_cpy = list(list_org)
# list_cpy = list_org[:]
# list_cpy.append('lemon')

# print(list_org)
# print(list_cpy)

mylist = [1, 2, 3, 4, 5, 6]
b = [x * x for x in mylist]
print(mylist)
print(b)
