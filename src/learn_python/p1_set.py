new_set: set[int] = set()
print(new_set, ":", type(new_set))


fruits = {"apple", "banana", "orange", "square"}
print(fruits)

fruits.add("papaya") # adds in random place. Sets are unordered
print(fruits)

#fruits.remove("pear") # error if not present
fruits.remove("apple")
print(fruits)

fruits.discard("pear") # safe remove 
print(fruits)

if "banana" in fruits:
    print ("i am a banana!")

print("======================================\n")
print(">>>>>>", fruits)

vegetables: set[int] = {
    "potato", "tomato", "cucumber", "square"
}
print(">>>>>>", vegetables)

print("union | :", fruits | vegetables)

print("intersection & :", fruits & vegetables)

print("difference - :", fruits - vegetables)

print("sym diff ^ :", fruits ^ vegetables)

