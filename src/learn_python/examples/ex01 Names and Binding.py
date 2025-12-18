

numbers = [1, 2, 3]
alias = numbers            # alias references the same list
copy_numbers = numbers[:]  # shallow copy

# Mutate through alias
alias.append(4)

# Rebind numbers to a new list
numbers = [10, 20, 30]

print(alias)
print(numbers)

# Compare identity and equality
print("alias is numbers:", alias is numbers)
print("alias == numbers:", alias == numbers)
print("alias is copy_numbers:", alias is copy_numbers)
print("alias == copy_numbers:", alias == copy_numbers)