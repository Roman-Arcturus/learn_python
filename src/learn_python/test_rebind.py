# Rebinding vs Safe Copy

global_list = [111, 222, 333, 444, ]

def mutate_list(in_list, in_val):
    inner = in_list        # rebinding doesn't prevent
    inner.append(in_val)   # mutating of the original list
    return inner
    
def safecopy_list(in_list, in_val):
    inner = in_list.copy()    # making a safe copy. inner points to a new, local list
    # inner = list(in_list)   # making a safe copy, variant 2. list() - materializes a copy
    inner.append(in_val)      # modifying the local list wont mutate the original
    return inner

print("\nRebinding doesnt prevent mutating:")
print(f'Global list: {global_list} before calling the func mutate_list()')
new_list = mutate_list(global_list, 12345)
print("The state after calling the function:")
print(f'Global list: {global_list}. Return list: {new_list}')

print("\nSafe copy prevents mutating")
print(f'Global list: {global_list} before calling the func safecopy_list()')
new_list = safecopy_list(global_list, 100500)
print("The state after calling the function:")
print(f'Global list: {global_list}. Return list: {new_list}')
