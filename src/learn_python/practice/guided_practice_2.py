# ——— ——— ——— Guided Practice — Continue 1  ———  ———  ———

"""
Goal: Reduce passes without losing clarity or safety
You correctly identified earlier that your current solution has three passes:
. Validate container + element structure
. Extract a simple list[int]
. Filter + transform

This is correct, safe, and readable.
Now we explore when and how to collapse passes intentionally.

Step 1 — Restate the functional contract (unchanged)

We do not change behavior.
Constraints stay fixed.
Only mechanics change.
"""

"""
Step 2 — Observation (important)

You already noticed this:
. Structural validity is all-or-nothing
. Semantic eligibility is per-record

That gives us permission to:
. Fail fast on structure
. Stream semantic filtering

This means:
. One short-circuiting structural pass
. One single computation pass
"""

"""
Step 4 — Your task (do not skip this)

Write one function that:
Performs exactly one full pass over records

Still:
. fails fast if a non-dict is encountered
. ignores invalid records
. returns a new list
. never raises

You may use:
. a for loop
. local variables
. append
. early return

You may not:
. use exceptions for control flow
. pre-build intermediate lists
. mutate input
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
    #100500,                                             # record not a dict
]

def process_amounts_single_pass(records) -> list[int]:
    """
    I.   If records is not a list → return []
    II.  If any element is not a dict → return []
    III. Records without "amount" → ignore
    IV.  Records where "amount" is not an int → ignore
    V.   From remaining:
        - keep positive, even integers
        - scale by 10
    VI.  Do not mutate input
    VII. No exceptions escape
    """
    
    if not isinstance(records, list): # I.
        return []

    result: list[int] = []

    for record in records:
        # structural validity (fatal)
        if not isinstance(record, dict): # II.
            return []

        # semantic eligibility (non-fatal)
        if (
            "amount" in record # III.
            and type(record["amount"]) is int # IV.
            and is_positive(record["amount"])
            and is_even(record["amount"])
        ):
            result.append(scale_by_10(record["amount"]))

    return result

# end def ——— ——— ———


#for each in inventory:
#    print(each)


result = process_amounts_single_pass(inventory)
print(result)

