def add_num(a: int, b: int) -> int:
    return a + b

def f(a, b, /):
    return b - a

print(f(12, 23))

def connect(host: str, *, timeout: int = 30):
    return f"{host}  >> t/o: {timeout}"

print(connect("https://omnomnom.com", timeout=777))

def add_all(*numbers):
    return sum(numbers)

print("add_all: " , add_all(1,2,3) )


def create_user(name, **kwargs):
    print("Required:", name)
    print("Optional settings:", kwargs)

create_user(
    "Alice",
    age=30,
    is_admin=True,
    email="alice@example.com"
)

create_user("cookie")


def circle_area(radius: float) -> float:
    """
    Compute area of a circle.

    Parameters
    ----------
    radius: float
        Radius in meters.

    Returns
    -------
    float
        Area in square meters.
    """
    return 3.14 * radius * radius

#print( "area of circle: ", circle_area(3) )
#print( "help of function: ", help(circle_area))


def user_info(name:str, age:int) -> dict:
    return {
        "name": name, 
        "age": age
    }

print( user_info("Arthur", "33") )


def add_item(lst):
    lst.append(99)

nums = [1, 2, 3]
add_item(nums)
print(nums)  # [1, 2, 3, 99]
add_item(nums)
print(nums)  # [1, 2, 3, 99, 99]

print("\n-------------------------------")

def replace_list(lst):
    lst = [9, 9, 9]   # rebinding (no effect outside)

def mutate_list(lst):
    lst.append(4)     # mutation (affects caller)

items = [1, 2, 3]
replace_list(items)
print(items)  # [1, 2, 3]

mutate_list(items)
print(items)  # [1, 2, 3, 4]

def f(lst):
    lst = [100]      # rebinding
    lst.append(200)

data = [1, 2, 3]
f(data)
print(data)


#Fix the function so it does not modify the caller's list:

values: list = [100, 200, 400, 300, 11]
def clean(data):
    data.sort()
    return data

#print (values)
#print(clean(values))
#print (values)

values: list = [100, 200, 400, 300, 11]
def clean_2(data:list) -> list:
    data_copy: list = data.copy()
    data_copy.sort()
    return data_copy

print (values)
print( clean_2(values) )
print (values)


class Box:
    def __init__(self, value):
        self.value = value

def update(box:object) -> int:
    box.value += 1

b = Box(55)
print(b.value)
x = Box(222)
print(b.value)
print(x.value)

#print(b.value)
#x = update(b)
#print(b.value)

#print("b= ", b.value, " x= ", x.value)

