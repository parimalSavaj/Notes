a = int(input("Enter a number: "))
b = int(input("Enter b number: "))

if ( b == 0):
    raise ZeroDivisionError("we not division to zero ")
else:
    print(a/b)