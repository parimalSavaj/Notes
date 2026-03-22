from functools import reduce

l = [1,2,3,4,5]

# map

square = lambda x: x*x # lambda function

sqList = map(square,l) # map

print(list(sqList))

# filter

def even(n):
    if(n%2 == 0):
        return True

onlyEven = filter(even,l)
print(list(onlyEven))

# reduce
def sum(a,b):
    return a+b

print(reduce(sum,l))
