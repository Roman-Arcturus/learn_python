## Code / Execution

numbers = [1, 2, 3]

# Late-binding bug: loop variable captured directly
funcs_bug = [
    lambda: numbers[i] * 2 
    for i in range( len(numbers) )
]

# Defensive closure: capture current value via default argument
funcs_safe = [
    lambda x = numbers[i]: x * 2 
    for i in range( len(numbers) )
]

# Execute functions
bug_results = [ f() for f in funcs_bug ]
safe_results = [ f() for f in funcs_safe ]

print("Late-binding bug results:", bug_results)
print("Defensive closure results:", safe_results)

