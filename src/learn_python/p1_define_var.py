# 1. Variables (Core Concept)

x = 10
y = "hello"
z = 3.14

# proper way:
count: int = 10
message: str = "hello"
temperature: float = 21.5

full_dict: dict = {}
user: dict = {
    "name": "Roman",
    "age": 40,
    "is_active": True,
    "waza": "yo"
}

new_list: list[int] = []
values = [1, 2, 3]

new_set: set[int] = set()
fruits = {"apple", "banana", "orange", "square"}




# 2. Primitive Types (Most Important)

"""
int	    1, 0, -5	        arbitrary           precision
float	2.5, 3.14, -0.01	IEEE-754            double
bool	True, False	        boolean             type
str	    "hello", "Roman"	immutable Unicode   strings
None	None	            means “no value”
"""

# 3. Expressions (How values are computed)

"""
--- Numeric operations ---
a + b
a - b
a * b
a / b   # float division
a // b  # integer division
a % b   # modulus
a ** b  # power
"""

"""
--- String operations ---
"Hello " + "world"
"Repeat " * 3
"""

"""
--- Comparison ---
a == b
a != b
a > b
a <= b
"""

"""
--- Logical ---
True and False
True or False
not True
"""

