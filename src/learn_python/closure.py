
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

# ——— ——— ——— Lesson 31 ——— ——— ——— 

def make_multipliers(numbers: list[int]) -> list[callable]:
    funcs = []

    for n in numbers:
        def multiply(x: int) -> int:
            return x * n

        funcs.append(multiply)

    return funcs

multipliers = make_multipliers([2, 3, 4])
# late binding to the last value, n is equal 4 for all cases

result_1 = multipliers[0]
result_2 = multipliers[1]
result_3 = multipliers[2]

print(result_1(2), result_2(2), result_3(2) )
# ->  8 8 8

# # bind the needed value **into the inner function at definition time**
def make_multipliers(numbers: list[int]) -> list[callable[int], int]:
    
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
# ->  4 6 8

multipliers = make_multipliers([5])

result_4 = multipliers[0]

print(result_1(2), result_2(2), result_3(2) )
# ->  4 6 8

print(result_4(2))
# ->  10

exit()

# ——— ——— ——— Closures as configuration ——— ——— ——— 

def make_threshold_checker(threshold: int) -> callable[[int], bool]:
    def is_above(value: int) -> bool:
        return value > threshold

    return is_above

peak_limit = 42
check_level = make_threshold_checker(peak_limit) 
# provide limit value once at the execution of the script

# then, during the script run we test some changing value 
# towards the constant defined once
#if check_level(current_value):
#    ...


# ——— ——— ——— Closures can accidentally capture **mutable objects**

# provided example:
def make_allowed_checker(allowed: set[int]):
    allowed.add(99) 
    def is_allowed(value: int) -> bool:
        return value in allowed

    return is_allowed

# usage example:
allowed_vals = {22, 33, 44} # defining a set in a config file for example
check_allowance = make_allowed_checker(allowed_vals) # creating a closure

# during the runtime we get unexpected result and obscure behaviour
print(check_allowance(22)) # True
print(check_allowance(99)) # should be False but is_allowed mutated global set


