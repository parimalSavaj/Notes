class Parent:
    def __init__(self):
        print("parent constructor call")
    

class Child1(Parent):
    def __init__(self):
        super().__init__()
        print("child1 constructor call")
    

class Child2(Child1):
    def __init__(self):
        super().__init__()
        print("child2 constructor call")
    

ch = Child2()
