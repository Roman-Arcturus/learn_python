# Task 5 (Semantic Tightening)

"""New focus

Distinguish clearly between:
Structural validity (can this record be processed?)
Semantic eligibility (should this record be included?)

New requirement
Add one additional rule:

A record with "value": 0 is considered structurally valid
but semantically ineligible and must be excluded from the result.

This rule must be:

Expressed in code (not comments)
Placed in the correct logical layer
Not break any existing behavior"""

"""Goal

Refactor the list comprehension only so that:
Structural checks are grouped and visually obvious
Semantic checks are grouped and visually obvious
Behavior is unchanged
"""

"""Constraints

Do not add new helper functions
Do not change the boundary checks
Do not add intermediate variables
Do not add comments explaining what the rule is — the code should make it obvious"""

"""Your task

Modify only the list comprehension accordingly."""


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
    { 'id': 11, 'title': 'Avocado',  'value': False, },
    { 'id': 12, 'title': 'Cucumber', 'value': {}, },
    { 'id': 13, 'title': 'Banana',   },    
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

    # --- Internal Computation ---
    
    return [
        scale_by_10(item["value"])
        for item in items
        if (
            ("value" in item)
            and type(item["value"]) is int
        ) 
        and (
            is_positive(item["value"])
            and is_even(item["value"])
        )
    ]
result = process_values(inventory)
print(result)

for each in inventory:
    print(each)

