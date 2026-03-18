# Two type of type conversion inside python.

# 1. Implicit: python automatically converted lower data-type to higher data-type

# example:

int_num = 10;
float_num = 10.5;
result = int_num + float_num; # here int_num variable type change int to float and then sum happen. but it's main type not change.

# type hierarchy: int -> float -> complex.


#2. explicit: we manually convert.

# we convert type using functions. below common type conversion functions:

# int(x, base) base option
# float(x)
# bool(x)
# list(x), tuple(x), set(x), dict(x)