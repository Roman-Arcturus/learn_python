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
    100500,                                             # record not a dict
]

def process_amounts(records: Any, log= None) -> list[int]:
    if log is None:
        def log(_: str) -> None:
            pass    

    errors: list[str] = []
    result: list[int] = []

    if not isinstance(records, list):
        log("records is not a list")
        return [], errors # fatal

    for i, record in enumerate(records):
        if not isinstance(record, dict):
            log(f"record[{i}] is not a dict")
            return [], errors  # fatal

        if "amount" not in record:
            continue

        if type(record["amount"]) is not int:
            log(f"record[{i}].amount == {record['amount']} / is not int")
            continue

        amount = record["amount"]

        if is_positive(amount) and is_even(amount):
            result.append(scale_by_10(amount))

    return result

g_error_list = []
def logging(error: str) -> None:
    g_error_list.append(error)

values, errors = process_amounts(inventory, log= logging)
print('values: ', values)


for each in g_error_list:
    print(each)
