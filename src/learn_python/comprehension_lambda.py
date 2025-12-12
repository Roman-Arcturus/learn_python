"""
lambda expression in Python is an inline, anonymous function.

# Example:
        lambda x: x * 2
This represents a function that takes x and returns x*2.

Lambda is a small function whose only purpose is:
“Extract or transform some property of this element at this specific moment.”
"""

users = [
    {"name": "Alice",   "active": True,  "meta": {"score": 10}},
    {"name": "Kevin",   "active": True,  "meta": {"score": 7}},
    {"name": "Bob",     "active": False, "meta": {"score": 5}},
]

# Sort the List users by name
result = sorted(
    users,
    key = lambda u: u["name"]
)

# Sort the List users by score, descending, in one line
result = sorted( users, key=lambda u: u["meta"]["score"], reverse = True )

# Get the Dict containing max score
result = max(
    users,
    key = lambda u: u["meta"]["score"]
)

# Get the Dict containing shortest name width defensive get
result = min(
    users,
    key = lambda z: len( z.get("name", "") )
)

# Filter the list where active = True
result = filter(
    lambda u: u["active"],
    users
)
# result will contain an object holding all the Dicts and can not be accesses directly

# gets only the fields chosen by lambda, returns an object with resulted values
result = map(
    lambda u: u["meta"]["score"],
    users
)

# ——— ——— ——— ——— ——— ——— Exercises ——— ——— ——— ——— ——— ———


# ——— Exercise 1 — Sorting by Score ———

# Sort users by score (ascending) using sorted() and a lambda.
result = sorted(users, key=lambda u: u["meta"]["score"])


# ——— Exercise 2 — Sorting by Name Length ———

# Sort users by the length of their name.
# Write the comprehension that extracts the sorted names.
result = [
    u["name"]
    for u in sorted(
        users, key=lambda u: len(u["name"])
    )
]

# ——— Exercise 3 — Filtering Active Users ———

#Use filter() with a lambda to keep only active users.
#Convert the result back to a list.
result = list( filter(lambda u: u["active"], users) )


# ——— Exercise 4 — Extract Scores via map() ———

#Use map() with a lambda to produce: [10, 5, 7]
result = list(
    map(lambda u: u["meta"]["score"], # extracts only the scores
        sorted(
            users,
            key = lambda u: u["meta"]["score"],
            reverse = False
        )
    )
)


# ——— Exercise 5 — Combine lambda + list comprehension ———

# Produce a list of user names whose score is greater than 6, using:
# list comprehension #and inside it, a lambda expression used to access the score
# End result: ["Alice", "Kevin"]

result = list(
    u["name"]
    for u in users
    if ( lambda x: x["meta"]["score"] )(u) > 6
)
#(lambda x: x["meta"]["score"])(u) -> create Lambda and Executes it

"""
Quick refresher: all() and any()

all(iterable) → bool
Returns True iff every element of iterable is truthy.
Short-circuits on the first falsy element.

any(iterable) → bool
Returns True iff at least one element of iterable is truthy.
Short-circuits on the first truthy element.

Important: both accept any iterable (generator, map, filter);
you do not need to wrap with list().
"""
all(x > 0 for x in [1,2,3])   # True
any(x > 2 for x in [1,2,3])   # True
all([])                       # True (vacuously true)
any([])                       # False


#print(result)

#for each in result:
#    print(each)

