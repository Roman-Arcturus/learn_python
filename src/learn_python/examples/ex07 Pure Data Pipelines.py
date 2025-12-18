## Code / Execution

numbers = [1, 2, 3, 4, 5]

# Step 1: Filter out even numbers
filtered = [
    n
    for n in numbers
    if n % 2 != 0
]

# Step 2: Double the remaining numbers
doubled = [
    n * 2
    for n in filtered
]

# Step 3: Convert to strings
stringified = [
    str(n)
    for n in doubled
]

print("Original:", numbers)
print("Filtered:", filtered)
print("Doubled:", doubled)
print("Stringified:", stringified)