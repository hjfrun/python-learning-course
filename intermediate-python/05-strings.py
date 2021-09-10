# Strings: ordered, immutable, text representation

# my_string = "Hello world"
# my_string = """Hello \
# world"""
# print(my_string)

# my_string = "Hello World"

# char = my_string[0]
# my_string[0] = 'h'
# substring = my_string[1:5]
# print(substring)

# greeting = "Hello"
# name = "Tom"
# sentence = greeting + " " + name
# print(sentence)

# for x in greeting:
#     print(x)

# if "ello" in greeting:
#     print("yes")
# else:
#     print("no")

# mystring = "     Hello world    "
# mystring = mystring.strip()
# print(mystring)

# my_string = "Hello World"
# print(my_string.lower())
# print(my_string.upper())
# print(my_string.startswith("He"))
# print(my_string.endswith("ld"))
# print(my_string.find("o"))
# print(my_string.find("p"))
# print(my_string.count("o"))
# print(my_string.replace("World", "Universe"))

# my_string = "how are you doing"
# my_string = "how,are,you,doing"
# my_list = my_string.split(",")
# print(my_list)

# new_string = " ".join(my_list)
# print(new_string)

# from timeit import default_timer as timer

# my_list = ["a"] * 1000000
# print(my_list)

# bad python code
# start = timer()
# my_string = ""
# for i in my_list:
#     my_string += i
# stop = timer()
# print(stop - start)

# good way

# start = timer()
# my_string = "".join(my_list)
# stop = timer()
# print(stop - start)

# var = "Tom"
# my_string = "The variable is %s" % var
# print(my_string)

# var = 3.14159
# my_string = "The vaiable is %.2f" % var
# print(my_string)

var = 3.14159
age = 31
# my_string = "The variable is {:.2f} and age {}".format(var, age)
my_string = f"The variable is {var * 2} and age {age}"

print(my_string)
