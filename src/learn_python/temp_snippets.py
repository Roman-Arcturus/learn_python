"""
orders = list(
    {
        "id": 1,
        "name": "apples",
        "price": 10, 
        "quantity": 2
    }, 
    {
        "id": 2,
        "name": "oranges",
        "price": 5, 
        "quantity": 3
    }
)
"""

orders:list = [
    {
        "id": 1,
        "name": "apples",
        "price": 10,
        "quantity": 2
    },
    {
        "id": 2,
        "name": "oranges",
        "price": 5,
        "quantity": 3
    },
]





def fun_square(x):
    return x * x
def fun_cube(x):
    return x * x * x

#My understanding is that we can create new reference to a function:
new_reference = fun_square  # creates another reference only
print( new_reference(10) )   # executes function stored in nrew_reference variable

#the references can be stored in lists. (Maybe in set and dict as well, but we'll see)
list_of_func = []
list_of_func.append(fun_square)
list_of_func.append(fun_cube)

#print( list_of_func )
#print(type(list_of_func)) # list

#list_of_func[0]     # keeps reference to fun_square()
#list_of_func[0](2)  # executes fun_square(2)

print( list_of_func[0](9) ) # prints 81
print( list_of_func[1](4) ) # executes fun_cube(4), prints 64

#this is my understanding that
#multipliers[i] is a function, not a value
#Only multipliers[i](x) produces a value.

