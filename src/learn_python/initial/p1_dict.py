import copy

new_dict = {}
print(new_dict, ":", type(new_dict), " ------- ")

full_dict : dict = {}


user = {
    "name": "  ROman  ",
    "age": 40,
    "is_active": True,
    "waza": "yo"
}

def normalize_w(user: dict) -> dict:
    user["name"] = user["name"].strip().title()
    user["active"] = True
    return user


# Python passes references.
def normalize(user: dict) -> dict:
    l_user = copy.deepcopy(user)
    
    name: str = l_user.get("name", "")
    l_user["name"] = name.strip().title()
    
    l_user["active"] = True
    return l_user

product_list: list[ dict ] = []

product_list.append({
    "id" : 1,
    "name" : "lamp",
    "price" : 10,
    "tags" : {"x1", "x22"}
})
product_list.append({
    "id" : 2,
    "name" : "kettle",
    "price" : 220,
    "tags" : {"y7", "y78"}
})


#users:list = [ dict ]

users = [
    {"name": "Alice", "active": False},
    {"name": "Bob",   "active": False},
]

def flip_all_users(users: list) -> list:
    result: list = []

    for u in users:
        name: str = u["name"]
        was_active: bool = u["active"]

        new_user: dict = {
            "name": name,
            "active": not was_active
        }

        result.append(new_user)

    return result


def toggle_all(users: list[dict]) -> list[dict]:
    """Return a new list with each user's 'active' value inverted."""
    result: list[dict] = []
    for u in users:
        result.append({"name": u["name"], "active": not u["active"]})
    return result


users = [
    {"name": "Alice", "score": 10},
    {"name": "Bob"},
    {"name": "Charlie", "score": 5}
]

def normalize_scores(users: list) -> list:
    """
    Return a new list of users dicts.
    Each new user will always contain "score", even if the input did not.
    """
    result:list[dict] = []
    
    for u in users:
        name = u["name"]
        score = u["score"] if "score" in u else 0
        
        new_u: dict = {
            "name" : name,
            "score" : score
        }
        result.append(new_u)

    return result

print(users)
print( normalize_scores(users))
print(users)

exit()



#print(users)
#print( flip_all_users(users) )
print(users)

exit()

def activate_all(users: list) -> list:
    result: list = []

    for u in users:
        new_u = {
            "name": u["name"],
            "active": True
        }
        result.append(new_u)

    return result






msg : str = ""
key : int = 0
value : str = ""

print(user["age"])

mas = user.get("email", "nope")
print(msg)

user["country"] = "Germany"     # add a field
user["age"] = 41                # modify a field

user.pop("waza")
print(user)

for key in user:
    print(key)
    
for value in user.values():
    print(value)

for key, value in user.items():
    print(key, ":", value)

if "name" in user:
    print("ma name is wa")

#Because dictionaries are mutable, modifying them inside functions affects the original.    
def activate(u: dict[str, bool]) -> None:
    u["is_active"] = True

user = {"is_active": False}
activate(user)
print(user["is_active"])

#Same behavior as lists: Python passes references.