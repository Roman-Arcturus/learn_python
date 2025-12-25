# Step 1 — Error Reporting without Exceptions
"""
Goal
Return results + structured error information, without:
. raising
. breaking pipelines
. relying on Python exceptions
. This mirrors exactly what you did in earlier systems.
"""

"""
Pattern: Result + Errors (explicit, cheap)
We introduce a convention, not a framework.
"""

from typing import Any

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
    100500,                                              # record not a dict
]

def process_amounts(
    records: Any
) -> tuple[list[int], list[str]]:
    """
    Returns:
        (result, errors)

    errors is empty if everything is fine.
    """

    errors: list[str] = []
    result: list[int] = []

    if not isinstance(records, list):
        errors.append("records is not a list")
        return [], errors # fatal

    for i, record in enumerate(records):
        if not isinstance(record, dict):
            errors.append(f"record[{i}] is not a dict")
            return [], errors  # fatal

        if "amount" not in record:
            continue

        if type(record["amount"]) is not int:
            errors.append(f"record[{i}].amount == {record['amount']} / is not int")
            continue

        amount = record["amount"]

        if is_positive(amount) and is_even(amount):
            result.append(scale_by_10(amount))

    return result, errors


(values, errors) = process_amounts(inventory)

print('values: ', values)
if errors:
    for each in errors:
        print(each)

