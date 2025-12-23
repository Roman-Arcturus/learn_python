"""
Compared to the previous exercise:
❌ We no longer require all-or-nothing validation at the record level
✅ We allow partial success
❌ Missing "value" is no longer fatal
❌ Non-int "value" is no longer fatal
✅ Invalid records are skipped
❌ Invalid input (not a list, non-dicts inside) is still fatal
"""

"""
# Constraints
Validate the outer boundary (items)
Avoid mutation
Avoid exceptions
Always return a list
Use pure helpers (is_positive, is_even, scale_by_10)
Keep the code readable and explicit
"""

"""
# Hints
You will still need isinstance(items, list)
You will still need isinstance(item, dict)
You may use "value" in item
You may use a single list comprehension
You must think carefully about the order of conditions

# Mental Model (Only One Sentence)
Boundary validation is still strict; record-level validation is now permissive.
Do not mix these two.
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
    { 'id': 1,  'title': 'Rose',     'value': 42, },
    { 'id': 2,  'title': 'Lyra',     'value': 1001, },
    { 'id': 3,  'title': 'Sunrise',  'value': 144, },
    { 'id': 4,  'title': 'Apples',   'value': -200, },
    { 'id': 5,  'title': 'Oranges',  'value': 155, },
    { 'id': 6,  'title': 'Kiwi',     'value': 0, },
    { 'id': 10, 'title': 'Avocado',  'value': True, },
    { 'id': 11, 'title': 'Cucumber', 'value': {}, },
    { 'id': 12, 'title': 'Banana',   },    
    #100500,
    #[],
]

# interface
def process_values(items:list[dict]) -> list[int]:
    """
    # Function Contract:
    . Receives a list of dicts.
    . Each dict may or may not contain a key "value".
    . If present, "value" must be an integer.
    . Return a new list of integers that are positive, even, and scaled by 10.
    . Invalid records should be ignored.
    . If the input itself is invalid, return an empty list.
    """
   
    # --- Boundary normalization ---

    # if input is not a list -> fatal, return empty list []
    if not isinstance(items, list): 
        return []

    # if not all records are dict -> fatal, return empty list []
    if not all( isinstance(item, dict) for item in items ):
        return []

    # copy only records w/ key name "value", that have value type int
    validated:list = [
        item 
        for item in items
        if ("value" in item)
        and type(item["value"]) is int 
    ]
    # instead of ("value" in item) -> item.get('value') to filter out value == 0
    # but all the logic needs to be in the Internal Computation
    
    # --- Internal Computation ---
    
    return [
        scale_by_10(item["value"])
        for item in validated 
        if is_positive(item["value"]) and is_even(item["value"])
    ]

result = process_values(inventory)
print(result)

for each in inventory:
    print(each)
