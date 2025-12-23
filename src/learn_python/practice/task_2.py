"""
You must: =>
Treat the function as a pipeline stage
Validate at the boundary
Use a validated snapshot
Use pure helpers
Avoid mutation
Avoid exceptions
Always return a list

You must not: =>
Introduce classes
Introduce exceptions
Use imports
Over-optimize

dict access: item["value"]
Safe key check: "value" in item
Type check: isinstance(x, int)
Snapshot validation applies to records, not values
Transformation applies only after validation
"""

# expected input data structure
inventory:list[dict] = [
    { 'id': 1, 'title': 'Rose',    'value': 300, },
    { 'id': 2, 'title': 'Lyra',    'value': 1001, },
    { 'id': 3, 'title': 'Sunrise', 'value': 144, },
    { 'id': 4, 'title': 'Apples',  'value': -200, },    
    { 'id': 5, 'title': 'Oranges', 'value': 155, },    
    { 'id': 6, 'title': 'Kiwi',    'value': 0, },   
    #100500
    #{ 'id': 12, 'title': 'Apples',   },
    #{ 'id': 13, 'title': 'Pears',  'value': [], },         
]

# helper predicate : return True if input int is even
def is_even(x: int) -> bool:
    return x % 2 == 0

# helper predicate : return True if input int is positive
def is_positive(x: int) -> bool:
    return x > 0

# helper transform : return input int * 10
def scale_by_10(x: int) -> int:
    return x * 10

# interface
def process_values(items:list[dict]) -> list[int]:
    """
    Receives a list of dicts, each expected to contain a key "value" 
    mapped to an integer. Returns a new list of integers that are 
    positive, even, and scaled by 10.
    On any invalid input, returns an empty list.
    """    
 
    # boundary input data type checks
    
    # if input is not list - early return
    if not isinstance(items, list): 
        return []
    
    # add dicts to a new list which contains field w/ key 'value' and int value
    validated = [
        n 
        for n in items
        if isinstance(n, dict) # ensure that element is a dict
        and ("value" in n) # can not use get('value'), because 0 -> "False"
        and type(n["value"]) is int 
        # can not use isinstance(n["value"], int), because bool True -> int
    ]
    
    # if lengths don't match, then input data types mismatch
    if len(validated) != len(items):
        return []
    
    # finally, process list with guaranteed type correctness
    return [
        scale_by_10(n['value'])
        for n in validated 
        if is_positive(n['value']) and is_even(n['value'])
    ]


result = process_values(inventory)
print(result)

for each in inventory:
    print(each)
