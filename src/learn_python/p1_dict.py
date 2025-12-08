user = {
    "name": "Roman",
    "age": 40,
    "is_active": True,
    "waza": "yo"
}

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