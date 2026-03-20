def my_printer():
    print("ok G")

my_printer()

# function with argument
def argFun(name):
    print(f"name = {name}")

argFun("parimal")

# function return value
def returnFun():
    print("ok sir")
    return "gg"

a = returnFun()
print(a)

# default arg
def defaultFun(name = 'savaj'):
    print(f"name = {name}")

defaultFun("pari")
defaultFun()
