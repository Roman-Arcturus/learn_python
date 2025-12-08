values = [1, 2, 3]

empty: list[int] = []

print(values)
print(empty)

values = list(range(5))

print(values)

values = [10, 222, 30, 40]
values[0]    # 10
values[2]    # 30

print(values[-2])

print(values[1])
values[1] = 999
print(values[1])

values.append(100500)
print(values)

values.insert(1, 555) #position, value
print(values)

print( values.pop() )     # removes last, returns it
print(values)

values.remove(999)  # removes first occurrence
print(values)

for value in values:
    print(value)
    
copy1 = values.copy()
copy2 = list(values)

print(copy1)
print(copy2)

copy3 = values[:] # [positions (from 0) start : end]

print(copy3)

if 555 in copy3:
    print("yep")

