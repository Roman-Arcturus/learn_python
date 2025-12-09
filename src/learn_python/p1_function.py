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
