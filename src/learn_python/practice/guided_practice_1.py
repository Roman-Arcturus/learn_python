# ——— ——— ——— Defensive Boundary + Clean Pipeline ——— ——— ———

#Scenario (Realistic Freelance Task)
"""
. You receive data from a legacy PHP system.
. The structure is mostly consistent, but not guaranteed.
. You must process it safely.
"""

# Input Description ——— ——— ———
"""
. records is supposed to be a list
. Each element is supposed to be a dict
. Some dicts contain "amount"
. "amount" may be missing
. "amount" may be non-int
. Valid "amount" values may include 0 (important)
"""

# Functional Contract ——— ——— ———
"""
. If records is not a list → return []
. If any element of records is not a dict → return []
. Records without "amount" → ignore
. Records where "amount" is not an int → ignore

From remaining records:
. keep positive, even integers
. scale each by 10
. Return a new list
. Do not mutate input
. No exceptions should escape the function
"""

# Constraints (Important) ——— ——— ———
"""
. No classes
. No try/except (for now)
. No external libraries
. Prefer clarity over cleverness
. At most two passes over the data
. Use helper functions if helpful
"""

# Hints (Syntax & Semantics) ——— ——— ———
"""
. "key" in dict is safer than dict.get() when 0 is valid
. type(x) is int vs isinstance(x, int) → choose deliberately
. and short-circuits left to right in Python
. List comprehensions are pipelines, not validation tools
. Boundary checks belong before computation
"""

# What NOT to Do ——— ——— ———
"""
. Do not validate and compute in one unreadable expression
. Do not assume inputs are friendly
. Do not raise exceptions
. Do not over-generalize
"""


# helper predicate : return True if input int is even
def is_even(x: int) -> bool:
    return x % 2 == 0

# helper predicate : return True if input int is positive
def is_positive(x: int) -> bool:
    return x > 0

# helper transform : return input int * 10
def scale_by_10(x: int) -> int:
    return x * 10

# expected input data structure
inventory:list[dict] = [
    { 'id': 1,  'title': 'Rose',     'amount': 42, },    # even amount
    { 'id': 2,  'title': 'Lyra',     'amount': 1001, },  # odd amount
    { 'id': 3,  'title': 'Sunrise',  'amount': 144, },
    { 'id': 4,  'title': 'Apples',   'amount': -200, },  # negative amount
    { 'id': 5,  'title': 'Oranges',  'amount': 155, },
    { 'id': 6,  'title': 'Kiwi',     'amount': 0, },     # amount == zero
    { 'id': 10, 'title': 'Avocado',  'amount': True, },  # `int` amount
    { 'id': 11, 'title': 'Avocado',  'amount': False, },
    { 'id': 12, 'title': 'Cucumber', 'amount': {}, },    # amount wrong type 
    { 'id': 13, 'title': 'Banana',   },                  # no field amount
    #100500,
    #[],
]

def process_amounts(records:any) -> list[int]:
    # Functional Contract ——— ——— ———
    """
    I. If records is not a list → return []
    II. If any element of records is not a dict → return []
    III. Records without "amount" → ignore
    IV. Records where "amount" is not an int → ignore

    From remaining records:
    . keep positive, even integers
    . scale each by 10
    . Return a new list
    . Do not mutate input
    . No exceptions should escape the function
    """

    # --- Boundary normalization ---

    # I. If records is not a list → return []
    if not isinstance(records, list): 
        return []

    # II. If any element of records is not a dict → return []
    if any(not isinstance(record, dict) for record in records):
        return []
        # 1st pass until the first non dict record encountered

    # copy amount value of records that contains key "amount" and value is int ONLY
    # fulfill Functional Contract -> III and IV
    filtered:list = [
        record["amount"]
        for record in records
        if ("amount" in record) 
        and type(record["amount"]) is int 
    ] # 2nd pass through complex list[dict] to create a simple list[int]

    # --- Internal Computation ---
    
    return [
        scale_by_10(amount)
        for amount in filtered
            if is_positive(amount) and is_even(amount)
    ] # 3rd pass - quick through the filtered:list[int]
    
# end def ——— ——— ———


for each in inventory:
    print(each)


result = process_amounts(inventory)
print(result)

