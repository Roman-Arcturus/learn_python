## Code / Execution

numbers = [1, 2, 3]

# Unsafe closure (late-binding)
funcs_unsafe = [
    lambda: numbers[i] * 2
    for i in range(len(numbers))
]

# Defensive closure using default argument
funcs_defensive = [
    (lambda x=numbers[i]: x * 2)
    for i in range(len(numbers))
]

# Testing
unsafe_results = [f() for f in funcs_unsafe]
defensive_results = [f() for f in funcs_defensive]

print("Unsafe results:", unsafe_results)
print("Defensive results:", defensive_results)

