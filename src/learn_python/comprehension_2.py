"""
We extend the foundational model:
        OUTPUT_EXPRESSION
            ← for ITEM in SEQUENCE
                ← optional FILTER

with two advanced capabilities:

1. **Inline conditional expressions (ternary operations)**

# Already used:
        for x in sequence if condition
            ...

# which is a filter, now add transformation logic:
        expression_if_true if condition else expression_if_false for x in sequence

# or write it in several lines:
        expression_if_true
        if condition
        else expression_if_false
        for x in sequence

# Embedded directly in the **output expression**, not the filter.

# example:
        normalized = [ n if n > 0 else 0 for n in nums ]


2. **Nested comprehensions as structured transformations**

# Already used this one:
        { tag   for u in users
                for tag in u["meta"]["tags"] }

# Mental model:
        [ inner_transform(x, y)
            for x in outer
            for y in inner(x)
                if some_condition(x, y) ]
"""


# ——— ——— ——— ——— ——— ——— Exercises ——— ——— ——— ——— ——— ———


# ——— Exercise 1 — Inline Conditional Expression ———
nums = [3, -2, 5, -1, 0]

# Produce a list where elements < 0 are replaced with 0
abs_val = [
    0
    if n < 0
    else n
    for n in nums
]

# ——— Exercise 2 — Tag Normalization Pipeline ———
users = [
    {"name": "Alice", "tags": ["x", "y"]},
    {"name": "Bob",   "tags": []},
    {"name": "Kevin", "tags": ["x", "z"]},
    {"name": "Kevin", "tags": ["a", "z"]},
]

# ——— Produce a Set of all tags that are NOT "x" ———
set_tags_not_x = {
    tag  for u in users
    for tag in u["tags"]
    if tag != "x"
}

# ——— Exercise 3 — Dict Comprehension with Inline Condition ———
nums = [1, 2, 3, 4, 5]

# Produce a dictionary: {1: "odd", 2: "even", 3: "odd", ...}
dict_oddness = {
    n : "even"
    if n % 2 == 0
    else "odd"
    for n in nums
}

# ——— Exercise 4 — Normalizing Nested Lists ———
matrix = [
    [1, -2, 3],
    [-1, 0, 4],
]

# Produce a flattened list of absolute values: [1, 2, 3, 1, 0, 4]
flat_abs_matrix: list = [
    abs(inner)
    for outer in matrix
    for inner in outer
]


# ——— Exercise 5 — defensive defaults ———
users = [
    {"name": "Alice",  "meta": {"tags": ["a", "b"]}},
    {"name": "Bob",    "meta": {"tags": []}},
    {"name": "Kevin",  "meta": {}},
    {"name": "Martha"},
]

# Create a list of: ["Alice: 2 tags", "Bob: 0 tags", "Kevin: 3 tags"]

exercise_5 = [
    (
        f"{u['name']}: {len(u.get('meta', {}).get('tags', []))} tags"
        if ("meta" in u and "tags" in u["meta"] and type(u["meta"]["tags"]) is list)
        else f"{u['name']}: 0 tags"
    )
    for u in users
]


