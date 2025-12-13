
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

#print( double(5) )  # 10
#print( triple(5) )  # 15


# ——— ——— ——— Exercise 18 — First Closure ——— ——— ———

"""Write a function make_adder(n)
Inside it, define a function add(x) that returns x + n
Return add
Create:
add_5 = make_adder(5)
add_10 = make_adder(10)
Call both with the same input and show different results"""

def make_adder(n):
    def add(x):
        return x + n
    return add
    
add_5 = make_adder(5)
add_10 = make_adder(10)

#print( add_5(3) )
#print( add_10(3) )

# ——— ——— ——— Closures — What Is Actually Remembered ——— ——— ——— 

# ——— ——— ——— Problematic example ——— ——— ———

funcs = []
for i in range(3):
    def f():
        return i
    funcs.append(f)

funcs[0]() # 2
funcs[1]() # 2
funcs[2]() # 2


# ——— ——— ——— Solution: introduce a new binding ——— ——— ———

funcs = []

for i in range(3):
    def make_f(n):
        def f():
            return n
        return f

    funcs.append(make_f(i))
    
funcs[0]()  # 0
funcs[1]()  # 1
funcs[2]()  # 2


# ——— ——— ——— Lesson 31 ——— ——— ——— 
numbers = []

def make_multipliers(numbers: list[int]) -> list[callable]:
    funcs = []

    for n in numbers:
        def multiply(x: int) -> int:
            return x * n

        funcs.append(multiply)

    return funcs

multipliers = make_multipliers([2, 3, 4])
# At this point: numbers == [2, 3, 4]
# The function body starts executing:
#   funcs = [], A new, empty list is created what will create functions
#   in the loop the functions are defined (not executed) and stored in multiply
#   after the loop finishes: funcs == [multiply, multiply, multiply]
#   These are three distinct function objects.
# so at this point the result is:
# multipliers == [
#    <function multiply>,
#    <function multiply>,
#    <function multiply>, ]

result_1 = multipliers[0]
result_2 = multipliers[1]
result_3 = multipliers[2]

print(result_1(2), result_2(2), result_3(2) )

# the fix
def make_multipliers(numbers: list[int]) -> list[callable]:
    funcs = []

    for n in numbers:
        def multiply(x: int, factor: int = n) -> int:
            return x * factor

        funcs.append(multiply)

    return funcs

multipliers = make_multipliers([2, 3, 4])

result_1 = multipliers[0]
result_2 = multipliers[1]
result_3 = multipliers[2]

print(result_1(2), result_2(2), result_3(2) )