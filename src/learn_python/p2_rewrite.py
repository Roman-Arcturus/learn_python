users = [
    {
        "name": "Alice",
        "meta": {
            "score": 10,
            "level": 1
        }
    },
    {
        "name": "Bob",
        # no meta
    },
]


def normalize_meta(users: list) -> list:
    result:list[dict] = []
    
    for u in users:
        name: str = u["name"]
        if "meta" in u:
            meta = u["meta"].copy()
        else:
            meta: dict = {}
            
        # Normalize fields
        score = meta["score"] if "score" in meta else 0
        level = meta["level"] if "level" in meta else 1            
        
        n_user: dict = {
            "name" : name,
            "meta" : meta
        }
        result.append(n_user)

    return result

def broken(users: list) -> list:
    result = []
    for u in users:
        meta = u.get("meta", {})
        meta["score"] = meta.get("score", 0)
        meta["level"] = meta.get("level", 1)

        new_u = {
            "name": u["name"],
            "meta": meta
        }
        result.append(new_u)

    return result

#print(users)
#print( normalize_meta(users))
print(users)
print( broken(users))
print(users)


#score = u["score"] if "score" in u else 0

print("------------ exit --------------")
exit()

def scale2(numbers, factor):
    for i in range(len(numbers)):
        numbers[i] *= factor
    return numbers

values:list = [1, 2, 3]
#scale(values, 2)
#print(values)


def scale(numbers: list, factor: int) -> list:
    l_list: list = []

    for i in range(len(numbers)):
        l_list.append( numbers[i] * factor )
    return l_list

values:list = [1, 2, 3, -4, -5]
print( scale(values, 2) )
print(values)


def remove_negative(nums: list) -> list:
    for i, n in enumerate(nums):
        if n < 0:
            nums[i] = 0
    return nums

def remove_negative(nums: list) -> list:
    l_list = nums.copy()
    for key, value in enumerate(l_list):
        if value < 0:
            l_list[key] = 0
    return l_list


print( remove_negative(values) )
print(values)


