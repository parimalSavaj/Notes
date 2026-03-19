# list just like array
a = ["savaj", "parimal", True, 1, 0.5]

# method of list

# to add element in last.
a.append("last")
print(a)

# add element in specific place.
a.insert(10, "any value we add")
print(a)

# remove last element and return this element 
b = a.pop()
# x = a.pop(2) # we also pop element with it's index number
print(b)

# remove give value inside list
c = a.remove(1) # don't return this value
print(c)

# d = a.remove(101) # give error if value not find inside list

# to sort list
# print(a.sort()) # but this support only integer and float

# reverse list
a.reverse()
print(a)

print(len(a))