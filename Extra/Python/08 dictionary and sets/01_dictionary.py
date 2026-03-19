dict = {
    "name":"parimal",
    "age": 18,
    0:123,
    True:[1,2,3]
}

print(dict)

# how to get data form this dict. for multiple way.

print(dict["name"])
print(dict[0])
# print(dict["names"]) # if not key found this so get error
print(dict.get("name"))
print(dict.get(0))
print(dict.get("names")) # using get method if key not found so return 'None'

# method of dic.
print(dict.items())
print(dict.keys())
print(dict.values())