## Code / Execution

# Immutable integers
a = 100
b = 100

print("a == b:", a == b)
print("a is b:", a is b)

# Mutable lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]  # same value, different object
alias = list1      # shared reference

print("list1 == list2:", list1 == list2)
print("list1 is list2:", list1 is list2)
print("list1 is alias:", list1 is alias)

# Mutate alias
alias.append(4)
print("After mutation:")
print("list1:", list1)
print("alias:", alias)
print("list2:", list2)
