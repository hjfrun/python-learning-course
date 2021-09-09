import json


# person = {
#     "name": "He Jianfeng",
#     "age": 31,
#     "city": "Shanghai",
#     "hasChildren": True,
#     "titles": ["engineer", "developer", "programmer"],
# }

# personJson = json.dumps(person, indent=4, sort_keys=True)
# print(personJson)

# with open("person.json", "w") as file:
#     json.dump(person, file, indent=4)

# person = json.loads(personJson)
# print(person)

# with open("person.json", "r") as file:
#     person = json.load(file)
#     print(person)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of the type is not JSON serializable")


# user = User("Jianfeng", 31)
# userJson = json.dumps(user, default=encode_user)
# print(userJson)


from json import JSONEncoder


class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)


user = User("Jianfeng", 31)
# userJson = json.dumps(user, cls=UserEncoder)
userJson = UserEncoder().encode(user)
print(userJson)


def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    return dct


# user = json.loads(userJson)
user = json.loads(userJson, object_hook=decode_user)
print(type(user))
print(user.name)
