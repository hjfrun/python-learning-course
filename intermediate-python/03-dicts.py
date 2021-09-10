# Dictionary : Key-Value pairs, Unordered, Mutable

mydict = {"name": "tengjiao", "age": 2, "city": "EZhou"}
# print(mydict)

# mydict2 = dict(name="jianfeng", age=31, city="Shanghai")
# print(mydict2)

# value = mydict["name"]
# print(value)

# mydict["email"] = "hale1007@qq.com"
# mydict["email"] = "hale1007@foxmail.com"
# print(mydict)

# del mydict["name"]
# print(mydict)

# mydict.pop("age")
# print(mydict)

# if "name" in mydict:
#     print(mydict["name"])

# try:
#     print(mydict["lastname"])
# except:
#     print("error")

# for key in mydict:
#     print(key)

# for key in mydict.keys():
#     print(key)

# for value in mydict.values():
#     print(value)

# for key, value in mydict.items():
#     print(key, value)

# mydict_cpy = mydict.copy()
# mydict_cpy["email"] = "hjf@a.com"

# print(mydict)
# print(mydict_cpy)

mydict2 = dict(name="hjf", age=31, email="hale1007@qq.com")

mydict.update(mydict2)
print(mydict)
