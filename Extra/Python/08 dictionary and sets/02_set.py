a = {1,2,3,4,4,4,"abcd",True, 5, 'a','ab'}
print(a)
print(type(a))

# output of set never comes same
# set con't contain duplicate values


# set methods.

# to add element in set
a.add(50)
print(a)

# remove element
a.remove(1)
print(a)

# pop
a.pop() # but not use this method
print(a)

b = {1,2,3,4,5}
c = {5,2,7,6,8}

print(b.union(c))
print(b.intersection(c))