class Number:
    def __init__(self, value):
        self.value = value

    # overload + operator
    def __add__(self, other):
        return Number(self.value + other.value)

# usage
n1 = Number(10)
n2 = Number(20)

result = n1 + n2   # calls __add__
print(result.value)

# What happened?
# n1 + n2 → Python internally calls:
# n1.__add__(n2)

# other operators method

# Operator	Method
#    +     	__add__
#    -      __sub__
#    *     	__mul__
#    /     	__truediv__
#    ==    	__eq__
#    <	    __lt__