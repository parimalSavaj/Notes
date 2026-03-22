class Parent:
    parent = "i am parent"

    def showParent(self):
        print(f"name of parent is {self.parent}")

class Child1(Parent):
    firstChildName = "child 1"

    def showFirstChild(self):
        print(f"first child name is {self.firstChildName}")

class Child2(Child1):
    secondChildName = "child 2"

    def showSecondChild(self):
        print(f"second child name is {self.secondChildName}")

ch = Child2()
ch.showParent()
ch.showFirstChild()
ch.showSecondChild()

print(f"parent = {ch.parent}")
print(f"child 1 = {ch.firstChildName}")
print(f"child 2 = {ch.secondChildName}")