x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()

outer()
# --> local

def outer():
    x = 10
    def inner():
        nonlocal x
        x += 1
        return x
    return inner()

print(outer())


def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc


c = make_counter()
print(c())
print(c())

x = "global"

def outer():
    y = "enclosing"

    def inner():
        z = "local"
        print(x, y, z)

    inner()

outer()
print(">>>>>>>>>>")

def outer():
    msg = ["hello"]

    def inner():
        print(msg[0])
        msg[0] = "changed"

    inner()
    print(msg[0])

outer()


x = 10  # Global

def outer():
    x = 20  # Enclosing
    def inner():
        x = 30  # Local
        print(x)
    inner()

outer()

x: int = 10
def outer():
    x = 20
    def inner():
        print(x)
    inner()

outer()


y = 50

def a():
    def b():
        print(y)
    b()

a()


def add_item(lst, item):
    lst.append(item)
    return lst

data = []
result = add_item(data, "x")

print(data)
print(result)