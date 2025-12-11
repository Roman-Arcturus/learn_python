users = [
    {"name": "Kevin",   "active": True,  "meta": {"score": 7}},
    {"name": "Alice",   "active": True,  "meta": {"score": 10}},
    {"name": "Bob",     "active": False, "meta": {"score": 5}},
]

# Exercise 1 — Sorting by Score
# Sort users by score (ascending) using sorted() and a lambda.
sort_score_asc: list = sorted(users, key=lambda u: u["meta"]["score"])

# Exercise 2 — Sorting by Name Length
# Sort users by the length of their name.
# Write the comprehension that extracts the sorted names.
names_extract: list = [
    u["name"] for u in sorted(users, key=lambda u: len(u["name"]) )
]

#Exercise 3 — Filtering Active Users
#Use filter() with a lambda to keep only active users.
#Convert the result back to a list.
filter_active = list ( filter(lambda u: u["active"], users) )

#Exercise 4 — Extract Scores via map()
#Use map() with a lambda to produce:
#[10, 5, 7]
list_scores_asc = list( map(lambda u: u["meta"]["score"],
    sorted(users, key=lambda u: u["meta"]["score"], reverse = False )
) )





#print( list_scores_asc )
