## Code Execution

# Mutable Default Trap
def add_item_trap(item, collection=[]):
    collection.append(item)
    return collection

result1 = add_item_trap(1)
result2 = add_item_trap(2)
result3 = add_item_trap(3)

# Safe alternative using None as default
def add_item_safe(item, collection=None):
    if collection is None:
        collection = []
    collection.append(item)
    return collection

safe1 = add_item_safe(1)
safe2 = add_item_safe(2)
safe3 = add_item_safe(3)

print("Mutable default trap results:", result1, result2, result3)
print("Safe alternative results:", safe1, safe2, safe3)
