nums = [1, 2, 3, 4, 5]

#Exercise 1 — Basic List Comprehension
#Produce a new list containing each number multiplied by 3.
multy_3 = [ n * 3 for n in nums ]

nums = [10, -1, 5, 0, -7, 2]

#Exercise 2 — Filtering
#Produce a list of only the positive numbers (greater than zero).
positive = [ n for n in nums if n > 0 ]

users = [
    {"name": "Alice", "active": True},
    {"name": "Bob", "active": False},
    {"name": "Kevin", "active": True},
    {"name": "Alice", "active": True},
]

#Exercise 3 — Transform + Filter
#Create a list of names of active users only.
list_active_users = [ u["name"] for u in users if u["active"] ]
set_active_users = { u["name"] for u in users if u["active"] }

print(list_active_users)
print(set_active_users)

users = [
    {"name": "Alice", "meta": {"score": 10}},
    {"name": "Bob", "meta": {"score": 1}},
    {"name": "Kevin", "meta": {"score": 5}},
]

#Exercise 4 — Dict Comprehension
#produce a dict {"Alice": 10, "Bob": 1, "Kevin": 5}
user_scores = { u["name"] : u["meta"]["score"] for u in users }


users = [
    {"name": "Alice", "meta": {"tags": ["a", "b"]}},
    {"name": "Bob",   "meta": {"tags": ["b", "c"]}},
]

#Exercise 5 — Nested Comprehension (Moderate)
#Produce a set of all unique tags. {"a", "b", "c"}
unique_tag_set = { tag for u in users for tag in u["meta"]["tags"] }

#print(unique_tag_set)

#print(user_scores)
#print( active_users )
#print(nums)
#print(multy_3)
#print(positive)
