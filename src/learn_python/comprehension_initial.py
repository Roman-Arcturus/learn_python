"""
A **comprehension** is a compact syntax for constructing a new
list / dict / set from an iterable by applying:
- iteration
- transformation
- optional filtering

Is the replacement of patters like this:
result = []
for x in items:
    if some_condition(x):
        result.append(process(x))

# → into this
result = [ process(x) for x in items if some_condition(x) ]

result = [ ... ]                → for creating a new list
result = { ... }                → a new set
result = { key: value for ... } → to create a dict
result = ( ... )                → for Generator expressions

OUTPUT_EXPRESSION
    ← for ITEM in INPUT_SEQUENCE
        ← optional FILTER
"""

# ——— ——— ——— ——— ——— ——— Examples ——— ——— ——— ——— ——— ———

nums: list = [1, 2, 3, 6]
users = [ { "name": "Alice", "active": True,
            "meta": { "score": 10, "tags": ["admin", "premium"] }
          },
          { "name": "Bob", "active": False,
           "meta": { "score": 12, "tags": ["level", "something"] }
          }, ]

# Basic transformation
squared = [ n * 2 for n in nums ]
# →  [2, 4, 6, 12]

# Basic filtering
evens = [ n for n in nums if n % 2 == 0 ]
# →  [2, 6]

# Mapping + Filtering
descriptions = [f"User: {u['name']}" for u in users if u["active"]]
# →  User: Alice

# Dict comprehension
scores = { u["name"]: u["meta"]["score"] for u in users }
# →  {'Alice': 10, 'Bob': 12}

# Set (only uniqes are saved) comprehension
unique_tags = { tag for u in users for tag in u["meta"]["tags"] }
# →  {'premium', 'admin', 'level', 'something'}


# ——— ——— ——— ——— ——— ——— Exercises ——— ——— ——— ——— ——— ———


# ——— Exercise 1 — Basic List Comprehension ———
nums = [1, 2, 3, 4, 5]

#Produce a new list containing each number multiplied by 3.
multy_3 = [ n * 3 for n in nums ]

# ——— Exercise 2 — Filtering ———
nums = [10, -1, 5, 0, -7, 2]

#Produce a list of only the positive numbers (greater than zero).
positive = [ n for n in nums if n > 0 ]

# ——— Exercise 3 — Transform + Filter ———
users = [
    {"name": "Alice",   "active": True},
    {"name": "Bob",     "active": False},
    {"name": "Kevin",   "active": True},
    {"name": "Alice",   "active": True},
]

#Create a list of names of active users only.
list_active_users = [ u["name"] for u in users if u["active"] ]

users = [
    {"name": "Alice",   "meta": {"score": 10}},
    {"name": "Bob",     "meta": {"score": 1}},
    {"name": "Kevin",   "meta": {"score": 5}},
]

# ——— Exercise 4 — Dict Comprehension ———
#produce a dict {"Alice": 10, "Bob": 1, "Kevin": 5}
user_scores = { u["name"] : u["meta"]["score"] for u in users }

# ——— Exercise 5 — Nested Comprehension (Moderate) ———
users = [
    {"name": "Alice", "meta": {"tags": ["a", "b"]}},
    {"name": "Bob",   "meta": {"tags": ["b", "c"]}},
]

#Produce a set of all unique tags. {"a", "b", "c"}
unique_tag_set = { tag for u in users for tag in u["meta"]["tags"] }

