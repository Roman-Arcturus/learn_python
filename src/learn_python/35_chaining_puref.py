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
    
print(user_tags(user_list))