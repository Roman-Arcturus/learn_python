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
    {
        "name": "Martha",
        "meta": {}
    },
    {
        "name": "Kevin",
        "meta": {
            "level": 3
        }
    },
    {
        "name": "Roman",
        "meta": {
            "score": 9
        }
    },
]


def normalize_meta(users: list) -> list:
    result:list[dict] = []

    for u in users:
        name: str = u["name"]

        if "meta" in u:
            meta: dict = u["meta"].copy()
            if "score" not in meta:
                meta["score"] = 0
            if "level" not in meta:
                meta["level"] = 1
        else:
            meta: dict = {
                "score" : 0,
                "level" : 1
            }

        n_user: dict = {
            "name" : name,
            "meta" : meta
        }
        result.append(n_user)

    return result

print(users)
processed: list = normalize_meta(users)

for value in processed:
    print(value)

#print(users[2])


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


