a = 5

def abc():
    a = 10
    print(a)

abc()
print(a)

def xyz():
    global a
    a = 15
    print(a)

xyz()
print(a)