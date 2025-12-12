users: list[dict] = [
    {"name": "Alice", "active": True,  "meta": {"score": 10}},
    {"name": "Bob",   "active": False, "meta": {"score": 3}},
    {"name": "Kevin", "active": True,  "meta": {"score": 7}},
]


"""
Goal:
Produce a list[str] containing formatted names of only active users:
["Alice (10)", "Kevin (7)"]

Pipeline steps:
    filter active users
    map each element to a formatted string
    convert final iterator to list

Use multi-line formatting and lambdas.
"""

# Exercise 1 — Filter → Map Pipeline
result = list(
    map(
        lambda u: f'{u["name"]} ({u["meta"]["score"]})',
        filter(
            lambda u: u["active"],
            users
        )
    )
)

"""
Goal: Produce a list[int] containing user scores sorted descending.
Result: [10, 7, 3]
"""
# Exercise 2 — sorted → map
result = list(
    map(
        lambda u: u["meta"]["score"],
        sorted(
            users,
            key = lambda u: u["meta"]["score"],
            reverse = True
        )
    )
)
"""
        users : list[dict]
        ↓ filter / sorted
        sorted(...) → list[dict]
        ↓ map
        map(...) → iterator[int]
        ↓ list
        list(...) → list[int]
"""



"""
Goal: Produce a list[str] of names of active users sorted by score descending.
Result: ["Alice", "Kevin"]
"""
# Exercise 3 — Combine filter + sorted + map
result = list(
    map(
        lambda u: u["name"],
        sorted(
            filter(
                lambda u: u["active"],
                users
            ),
            key = lambda u: u["meta"]["score"],
            reverse = True
        )
    )
)
"""
users : list[dict]
↓ filter
active_users : iterator[dict]
↓ sorted
active_sorted : list[dict]
↓ map
mapped_names : iterator[str]
↓ list
result : list[str]
"""

"""
Exercise 4 — any() and all()

You have:
scores = [10, 7, 3]

Produce the answers:
- any score above 8
- all scores above 2
- any score is exactly 0
- all scores are integers

Return the four answers in a tuple (a, b, c, d).
"""

scores = [0, 10, 7, 3]

def exercise_4(scores: list) -> tuple:
    all_int = all( isinstance(n, int) for n in scores )
    if not all_int:
        return (None, None, None, all_int)

    any_above_8 = any(n > 8 for n in scores)
    all_above_2 = all(n > 2 for n in scores)
    any_equal_0 = any(n == 0 for n in scores)

    return ( any_above_8, all_above_2, any_equal_0, all_int )

print(exercise_4(scores) )

"""
Exercise 5 — Build your first reusable higher-order function
Write a function:
        def pipe(data: Iterable, *functions):
            ...

What it must do:
Take input data.
Pass it through all functions in sequence.
Return the transformed result.
"""

def pipe(data, *functions):
    result = data
    for fn in functions:
        result = fn(result)
    return result


result = pipe(
    users,
    lambda data: filter(lambda u: u["active"], data),
    lambda data: sorted(data, key=lambda u: u["meta"]["score"], reverse=True),
    lambda data: map(lambda u: u["name"], data),
    list
)

"""
Important notes:
filter and map return iterators
sorted consumes the iterator and returns a list;
map later returns an iterator;
list finally materializes it.

pipe allows chaining functions that produce/consume iterables.
"""

print(result)

