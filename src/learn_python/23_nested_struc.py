user = {
    "name": "Alice",
    "meta": {
        "score": 10,
        "tags": ["admin", "premium"]
    }
}
user = {
    "name": "Alice",
}
user = {
    "name": "Alice",
    "meta": {}
}
user = {
    "name": "Alice",
    "meta": {
        "sscore" : 33
    }
}


def get_score(user: dict) -> int:
    if "meta" in user and "score" in user["meta"]:
        return user["meta"]["score"]

    return 0

#print( user )
#print( get_score(user) )
#print( user )



"""
But in real data, tags may be:
missing entirely
present but None
present but empty list
present but not a list (invalid input, e.g., a string)

**Requirements:**
1. Must return a NEW user dict (do not mutate original).
2. `"tags"` must always become a list inside `"meta"`.
3. If `"meta"` is missing, create it.
4. If `"tags"` is missing, set `[]`.
5. If `"tags"` is `None` or not a list, also set `[]`.
6. Preserve other fields as-is (e.g., `"score"`).
"""

user = {
    "name": "Alice",
    "meta": {
        "tags": ["admin", "premium"],
        "score": 10
    }
}
user = {
    "name": "Alice",
    "random" : "!@#!@#!@#",
    "meta": {
        "asdads" : 123,
        "tags" : None
    }
}

def normalize_tags(user: dict) -> dict:
    result: dict = user.copy()

    result["meta"] = { "tags" : [] }

    if "meta" in user:
        if type(user["meta"]) is dict:
            result["meta"] = user["meta"].copy()

            if "tags" in result["meta"]:
                if type(result["meta"]["tags"]) is not list:
                    result["meta"] = { "tags" : [] }
            else:
                result["meta"]["tags"] = []

    return result

print(user)
print( normalize_tags(user) )
print(user)
