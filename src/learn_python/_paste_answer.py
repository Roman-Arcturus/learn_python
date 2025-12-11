#Exercise 1 — Basic List Comprehension
#Produce a new list containing each number multiplied by 3.
multy_3 = [ n * 3 for n in nums ]

#Exercise 2 — Filtering
#Produce a list of only the positive numbers (greater than zero).
positive = [ n for n in nums if n > 0 ]

#Exercise 3 — Transform + Filter
#Create a list of names of active users only.
active_users = { u["name"] for u in users if u["active"] }

#Exercise 4 — Dict Comprehension
#produce a dict {"Alice": 10, "Bob": 1, "Kevin": 5}
user_scores = { u["name"] : u["meta"]["score"] for u in users }

#Exercise 5 — Nested Comprehension (Moderate)
#Produce a set of all unique tags. {"a", "b", "c"}
uniquie_tag_set = { tag for u in users for tag in u["meta"]["tags"] }
