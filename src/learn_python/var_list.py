#creates a list and put th reference into the list name
empty_list: list[int] = []
simple_list = []

listOf_int: list = [10, -1, 5, 0, -7, 2, -1, 5]

lisOf_list: list = [
    [111,   222,    333],
    [11,    22,     33],
    [1,     2,      3],
]

listOf_sets: list = [
    { 1, 3, 5 },
    { 2, 4, 6 },
]

listOf_dict: list = [
    {   "id" : 1,
        "name" : "Arthur",
        "role" : "Tank",
        "meta" : { "health" : 66, "stamina" : 30 },  },
    {   "id" : 5,
        "name" : "Sophya",
        "role" : "Rogue",
        "meta" : None, },
    {   "id" : 2,
        "name" : "Lorn",
        "role" : "Priest", },
]

# shalow copy
copy_v1 = listOf_dict.copy()
copy_v2 = list(listOf_dict)
copy_v3 = listOf_dict[:] # [positions (from 0) start : end]

# copy_vX holds a new reference to the top level list,
# but the references to internal mutables remain the same
# which can lead to Mutation if touched

# append a new element to the end of the list
listOf_sets.append("new element")

# insert a new element at a certain position
listOf_dict.insert(1, "new element")

# removes the last element of the list and returns its content
removed_elmt = listOf_int.pop()

# removes elements of the list with given value
listOf_int.remove(5)


