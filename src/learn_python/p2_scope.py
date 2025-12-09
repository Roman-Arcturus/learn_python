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