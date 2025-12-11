users = [
    {"name": "Alice",   "active": True,  "meta": {"score": 10}},
    {"name": "Kevin",   "active": True,  "meta": {"score": 7}},
    {"name": "Bob",     "active": False, "meta": {"score": 5}},
]

# Exercise 1 — Sorting by Score
# Sort users by score (ascending) using sorted() and a lambda.
sort_score_asc: list = sorted(users, key=lambda u: u["meta"]["score"])

#print(sort_score_asc)
#exit()

# Exercise 2 — Sorting by Name Length
# Sort users by the length of their name.
# Write the comprehension that extracts the sorted names.
names_extract: list = [
    u["name"] for u in sorted(users, key=lambda u: len(u["name"]) )
]

#Exercise 3 — Filtering Active Users
#Use filter() with a lambda to keep only active users.
#Convert the result back to a list.
filter_active = list( filter(lambda u: u["active"], users) )

#Exercise 4 — Extract Scores via map()
#Use map() with a lambda to produce:
#[10, 5, 7]
list_scores_asc = list( map(lambda u: u["meta"]["score"],
    sorted(users, key=lambda u: u["meta"]["score"], reverse = False )
) )


#Exercise 5 — Combine lambda + list comprehension
#Produce a list of user names whose score is greater than 6, using:
#list comprehension
#and inside it, a lambda expression used to access the score
#End result: ["Alice", "Kevin"]

great_score = [
    u["name"]
    for u in users
    if (lambda x: x["meta"]["score"])(u) > 6
]


print(great_score)

#if lambda a : u["meta"]["score"] > 6
#print( list_scores_asc )
