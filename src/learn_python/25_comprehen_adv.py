"""
Produce a list where:
negative numbers become 0
positive numbers remain unchanged
Use a list comprehension with inline condition.
"""

nums = [3, -2, 5, -1, 0]

#Exercise 1 — Inline Conditional Expression
#abs_val = [ n if n > 0 else 0 for n in nums ]

abs_val = [0 if n < 0 else n for n in nums]


"""
Produce a set of all tags that are NOT "x".

Expected:
{"y", "z"}

Use nested comprehension
filter inside comprehension
"""

users = [
    {"name": "Alice", "tags": ["x", "y"]},
    {"name": "Bob",   "tags": []},
    {"name": "Kevin", "tags": ["x", "z"]},
    {"name": "Kevin", "tags": ["a", "z"]},
]

#Exercise 2 — Tag Normalization Pipeline
set_tags_not_x = { tag for u in users for tag in u["tags"] if tag != "x" }


"""
Produce a dictionary:
{1: "odd", 2: "even", 3: "odd", ...}
Use a dict comprehension with inline conditional expression.
"""

nums = [1, 2, 3, 4, 5]

#Exercise 3 — Dict Comprehension with Inline Condition
dict_oddness = { n : "even" if n % 2 == 0 else "odd" for n in nums }



matrix = [
    [1, -2, 3],
    [-1, 0, 4]
]
"""
Produce a flattened list of absolute values:
[1, 2, 3, 1, 0, 4]
Use a nested list comprehension.
"""


#Exercise 4 — Normalizing Nested Lists
flat_abs_matrix: list = [ abs(inner) for outer in matrix for inner in outer ]



"""
Create a list of:

["Alice: 2 tags", "Bob: 0 tags", "Kevin: 3 tags"]

Rules:
use a list comprehension
use inline conditional expression ONLY if needed
no mutation of input
"""

users = [
    {"name": "Alice",  "meta": {"tags": ["a", "b"]}},
    {"name": "Bob",    "meta": {"tags": []}},
    {"name": "Kevin",  "meta": {}},
    {"name": "Martha"},
]

exercise_5: list = [
    f"{u['name']}: {len(u.get('meta', {}).get('tags', []))} tags"
            for u in users
]

exer_5 = [ f"{u['name']}: {len(u.get('meta', {}).get('tags', []))} tags"
               if ("meta" in u and "tags" in u["meta"] and
                   type(u["meta"]["tags"]) is list
                )
                else 0
                    for u in users
]

exercise = [
    "meta" in u and "tags" in u["meta"] and type(u["meta"]["tags"]) is list
    for u in users
]


exercise = [
    (
        f"{u['name']}: {len(u.get('meta', {}).get('tags', []))} tags"
        if ("meta" in u and "tags" in u["meta"] and type(u["meta"]["tags"]) is list)
        else f"{u['name']}: 0 tags"
    )
    for u in users
]




#print(users)
print(exercise)
#print(users)




userz = [
    {"name": "Alice", "meta": {"tags": ["a", "b"]}},
    {"name": "Bob",   "meta": {"tags": ["b", "c"]}},
]
#unique_tag_set = { tag for u in userz for tag in u["meta"]["tags"] }




#print( flat_abs_matrix )
#print( flat_abs_matrix )
#print(dict_oddness)
#print( set_tags_not_x )
#print( abs_val)
