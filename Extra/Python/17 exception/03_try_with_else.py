try:
    a = int(input("Enter number: "))
    print(a)
except ValueError as e:
    print("Enter valid number")
else:
    print("this is else part") # if error comes so this block not run!!
print("Thank you")