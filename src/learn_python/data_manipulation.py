# ——— ——— ——— Example 1 ——— ——— ———
nums = [3, -1, 4, 0, 7]

"""
Produce a list of absolute values, but only for positive inputs.
So from [3, -1, 4, 0, 7] you should produce:
[3, 4, 7]
"""

# Basic filtering
result = list(
    abs(x)
    for x in nums
    if x > 0
)

# Variant 1 — filter + map (functional chain)
result = list(
    map(
        lambda x: abs(x),
        filter(lambda x: x > 0, nums)
    )
)
# Filtering happens first, mapping afterward.
# This is good when operations need to be explicitly chained or reordered.

# Variant 2 — simple for-loop (baseline)
result = []
for x in nums:
    if x > 0:
        result.append(abs(x))

"""Plain loops remains essential in production code when:
you need debugging,
you need additional side logic,
a comprehension becomes unreadable,
condition chains become too complex.
But your instinct is correct: for pure data transformation,
comprehensions and functional chains are the modern norm.
"""

# ——— ——— ——— Example 2 — filter() + lambda ——— ——— ———
nums = [3, -1, 4, 0, 7]

#Produce a list of only the even numbers using a filter() call with a lambda.
#Target output: [4, 0]

result = list(
    filter(
        lambda x: x % 2 == 0,
        nums
    )
)

# ——— ——— ——— Example 3 — map() + lambda + numeric transform ——— ——— ———

# Produce a list of squares of all numbers using map() and lambda.

result = list(
    map(
        lambda x : x * x,
        nums
    )
)


# ——— ——— ——— Example 4 — filter() + map() + chained numeric transform ——— ——— ———

#Produce a list of absolute values, but only for odd numbers.

result = list(
    map(
        lambda z : abs(z),
        filter(
            lambda x : x % 2 != 0,
            nums
        )
    )
)

# ——— ——— ——— Example 5 — combining all() with filtering ——— ——— ———

#Check whether all positive numbers in the list are less than 10.

"""First extract only the positive numbers
Then apply all()
Use filter() and lambda
Use a multi-line structure
Output should be a single boolean value (True or False)"""

#output = boolean
nums = [3, -1, 4, 0, 7]

result: bool = all(
    z < 10 for z in filter(
        lambda z : z > 0,
        nums
    )
)

# ——— ——— ——— Example 6 — any() + map() + filter() ——— ——— ———

# Determine whether any number in the list becomes > 20 after doubling.

nums = [3, -1, 4, 0, 7]

"""Use filter() to take only positive numbers
Use map() to double them
Then apply any()
"""

result: bool = any(
    z > 20 for z in map(
        lambda y: y * 2,
        filter(
            lambda x: x > 0,
            nums
        )
    )
)


# ——— ——— ——— Exercise (7) choose between multiple possible transformations. ——— ——— ———

nums = [3, -1, 4, 0, 7, 12]

#Produce a list of strings describing each positive even number in the form:
#"VALUE is even"
#["4 is even", "12 is even"]

#Use filter to keep only positive & even numbers.
#Use map to transform numbers into the string format.

result = list(
    map(
        lambda z: f"{z} is even",
        filter(
            lambda y: y > 0 and y % 2 == 0,
            nums
        )
    )
)


# ——— ——— ——— Exercise (8) Combine 3 steps ——— ——— ———

nums = [3, -1, 4, 0, 7, 12]

#Produce a list of halved absolute values, but only for numbers greater than 5.
#[3.5, 6.0]


result = list(
    map(
        lambda z: abs(z) / 2,
        filter(
            lambda y: y > 5,
            nums
        )
    )
)


# ——— ——— ——— Exercise (9) filter → map → sorted in one expression ——— ——— ———

users = [
    {"name": "Alice", "score": 7},
    {"name": "Bob",   "score": 3},
    {"name": "Kevin", "score": 10},
    {"name": "Mara",  "score": 5},
]

# Produce a list of name-lengths, but only for users whose score is >= 5,
# and sorted by descending score.

#Use filter() to keep only users with u["score"] >= 5.
#Use sorted(..., key=..., reverse=True) to sort by score descending.
#Use map() to convert each user to len(u["name"]).

#Score ≥ 5 → Alice (7), Kevin (10), Mara (5)
#Sorted by score descending → Kevin, Alice, Mara
#Name lengths → [5, 5, 4]

result = list(
    map(
        lambda z: len(z["name"]),
        sorted(
            filter(
                lambda y: y["score"] >= 5,
                users
            ),
            key = lambda x: x["score"],
            reverse = True
        )
    )
)


# ——— ——— ——— Exercise (10) conditional logic inside lambda expressions. ——— ——— ———

users = [
    {"name": "Alice", "score": 7},
    {"name": "Bob",   "score": 3},
    {"name": "Kevin", "score": 10},
    {"name": "Mara",  "score": 5},
]

#Produce a list of strings in the following format:
#"<name>: PASS"   if score ≥ 5
#"<name>: FAIL"   otherwise
#["Alice: PASS", "Bob: FAIL", "Kevin: PASS", "Mara: PASS"]

#Use map() only (no filter, no sorted).
#The lambda must contain an inline conditional expression.

result = list(
    map(
        lambda u: f'{u["name"]} : PASS'
        if u["score"] >=5 else f'{u["name"]} : FAIL',
        users
    )
)

# ——— ——— ——— Exercise (11) — Lambda + Nested Data Extraction ——— ——— ———

products = [
    {"id": 1, "meta": {"price": 10, "tags": ["a", "b"]}},
    {"id": 2, "meta": {"price": 3,  "tags": []}},
    {"id": 3, "meta": {"price": 20, "tags": ["b", "c", "d"]}},
]

#Produce a list of strings of the form:
#"ID <id> / <num_tags> tags"
#["ID 1 / 2 tags", "ID 2 / 0 tags", "ID 3 / 3 tags"]

result = list(
    map(
        lambda p: f'ID {p["id"]} / {len(p["meta"]["tags"])} tags',
        products
    )
)


# Continue from data_manipulation.py

# ——— ——— ——— Exercise 12 — Predicate Discipline ——— ——— ———

nums = [2, -3, 0, 5, 8]

"""Produce a list of strings:
"2 is even"
"8 is even"
Use filter() to select only positive even numbers.
Use map() to format strings.
"""

result = list(
    map(
        lambda z: f'{z} is even',
        filter(
            lambda y: y > 0 and y % 2 == 0,
            nums
        )
    )
)

# ——— ——— ——— Exercise 13 — Reducer Thinking ——— ——— ———

nums = [3, 6, 9, 12]

"""Determine whether all positive numbers are divisible by 3.
Rules:
Use filter() to keep only positive numbers.
Use a generator expression (not map) inside all().
No list(...) wrapping.
"""

result: bool = all(
    z % 3 == 0 for z in filter(
        lambda y: y > 0,
        nums
    )
)

# ——— ——— ——— Exercise 14 — Choose the Better Tool ——— ——— ———
"""Produce a list of **squares of positive numbers**.

**Part A**
Write the solution using **filter + map**.

**Part B**
Write the solution using a **single list comprehension**."""
nums = [2, -3, 0, 5, 8]

#Part A
result = list(
    map(
        lambda z: z * z,
        filter(
            lambda y: y > 0,
            nums
        )
    )
)

#Part B
result = list(
    n * n
    for n in nums
    if n > 0
)


print(result)
