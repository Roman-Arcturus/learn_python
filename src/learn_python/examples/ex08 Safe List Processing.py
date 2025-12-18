## Code / Execution

numbers = [1, 2, 3, 4, 5, 6]

# Approach 1: Copy and mutate safely
copy_numbers = numbers.copy()

for i in range(len(copy_numbers)):
    copy_numbers[i] += 1  # simple mutation that preserves some odd/even mix
    
safe_mutated = [
    n for n 
    in copy_numbers 
    if n % 2 != 0
]

#Approach 2: Pure transformation
safe_transformed = [
    n + 1
    for n in numbers
    if (n + 1) % 2 != 0
]

print("Original:", numbers)
print("copy_numbers:", copy_numbers)
print("Safe Mutated Copy:", safe_mutated)
print("Safe Transformed:", safe_transformed)


