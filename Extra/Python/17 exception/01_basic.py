try:
    a = int(input("Enter number: "))
    print(a)
except ValueError as e:
    print("Enter valid number")
except Exception as e:
    print(e)
print("Thank you")