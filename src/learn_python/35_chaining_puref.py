orders = [
    {
        "id": 1,
        "items": [
            {"price": 10, "quantity": 2},
            {"price": 5, "quantity": 4},
        ],
    },
    {
        "id": 2,
        "items": [
            {"price": 20, "quantity": 1},
        ],
    },
]


#Step 1: extract totals per order (pure, explicit)
def order_total(order: dict) -> int:
    return sum(
        item["price"] * item["quantity"]
        for item in order["items"]
    )
    
#Step 2: build a pipeline over orders
def all_order_totals(orders: list[dict]) -> list[int]:
    return [
        order_total(order)
        for order in orders
    ]
    
#for each in all_order_totals(orders):
#    print(each)
    
#  ——— Defensive extraction from nested structures (without mutation)  ———  ———  ———

orders = [
    {
        "id": 1,
        "items": [
            {"price": 10, "quantity": 2, "discount": 0.1},
            {"price": 5, "quantity": 4},
        ],
    },
    {
        "id": 2,
        "items": [
            {"price": 20, "quantity": 1, "discount": 0.2},
        ],
    },
]

# Step 1: normalize one item (boundary function)
def normalized_item_total(item: dict) -> float:
    price = item["price"]
    quantity = item["quantity"]
    discount = item.get("discount", 0.0) # safe get

    return price * quantity * (1.0 - discount)

#Step 2: order-level aggregation
def order_total(order: dict) -> float:
    return sum(
        normalized_item_total(item)
        for item 
        in order["items"]
    )
    
#Step 3: pipeline across orders
def all_order_totals(orders: list[dict]) -> list[float]:
    return [
        order_total(order)
        for order in orders
    ]
    
#for each in all_order_totals(orders):
#    print(each)

#  ——— ——— ——— Exercise ——— ——— ———
    
user_list: list = [
    {"id": 1, "name": "Alice", "active": True, "tags": ["x", "y"]},
    {"id": 2, "name": "Bob",   "active": False, "tags": []},
    {"id": 3, "name": "", "active": True, "tags": ["x", "z"]},
    {"id": 4, "random": 100500},
]

#- Return `"unknown"` if `"name"` is missing or empty
def safe_user_name(user: dict) -> str:
    name = user.get("name")
    if not name:
        return "unknown"

    return name    

#- Return names of users where `"active" == True"`
def active_user_names(users: list[dict]) -> list[str]:
    return [
        safe_user_name(u)
        for u in users
        if u.get("active", False)
    ]    
    

if not "":
    print("empty string is treated as 'False'")
 
print(active_user_names(user_list))
    
#for each in active_user_names:
#    print(each)

    
"""Return the list under "tags" if present and non-empty
Otherwise return an empty list
Do not mutate the input
Do not raise exceptions
Use .get() and truthiness intentionally
Reply with only the function definition."""

def safe_tags(user: dict) -> list[str]:
    tags = user.get("tags")

    if not isinstance(tags, list) or not tags:
        return []

    return list(tags) # returns a safe copy

def user_tags(users: list[dict]) -> list[list[str]]:
    return [
        safe_tags(u)
        for u in users
    ]    
    
# print(user_tags(user_list))

# ——— ——— ——— Sorting as a pure transformation ——— ——— ——— 

users = [
    {"id": 1, "name": "Charlie"},
    {"id": 2, "name": "Alice"},
    {"id": 3, "name": "Bob"},
]

#Step 1: define the ordering rule (key function)
def user_name(user: dict) -> str:
    return user["name"]

#Step 2: apply sorting as a pipeline stage
def sort_users_by_name(users: list[dict]) -> list[dict]:
    return sorted(
        users,
        key = user_name
    )

#  ——— ——— ——— Exercise ——— ——— ———

orders:list = [
    {
        "id": 1,
        "name": "apple",
        "price": 10,
        "quantity": 4
    },
    {
        "id": 2,
        "name": "orange",
        "price": 5,
        "quantity": 3
    },
    {
        "id": 3,
        "name": "banana",
        "price": 1,
        "quantity": 2
    },
]

def order_total(item: dict) -> float:
    return item["price"] * item["quantity"]
    
def sort_orders_by_total(items: list[dict]) -> list[dict]:
    return sorted(    # sorted() returns a new list; input is not mutated
        items,
        key = order_total
    )
    
for each in sort_orders_by_total(orders):
    print(each)
    
for each in orders: # check if input list is mutated
    print(each)
    

#when learning about comprehensions with lambda, we used the pattern:
def transform_data():
    return list(
        map(
            lambda x:x, # -> output data transform rule
            sorted(
                filter(
                    lambda y:y, # -> filter rule
                    input_list
                ),
                key = lambda z:z  # -> the sorting condition is put directly 
            )
        )    
    )

"""
moving the sorting condition (as well as filtering one) to another functions, 
which can be changed later- is a logical next step. Now:
1. our functions are responsible for only one thing
2. our functions can be piped

As to answer your question:
>> Does the distinction between _projection_ (`key=`) and _ordering_ feel clear now?
I think I understand that sorted() only copies the overall structure of the input and
inserts to output list elements in the required order. It does not reorder input list.
"""

def is_valid(x):
    return bool(x)

def identity(x):
    return x

def transform_data(input_list):
    return list(
        map(
            identity,
            sorted(
                filter(
                    is_valid,
                    input_list
                ),
                key=identity
            )
        )
    )
