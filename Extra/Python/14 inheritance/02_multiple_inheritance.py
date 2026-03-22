class Parent1:
    name1 = "Parent 1"

    def showParent1(self):
        print(f"first parent name is {self.name1}")

class Parent2:
    name2 = "Parent 2"

    def showParent2(self):
        print(f"second parent name is {self.name2}")

class Child(Parent1, Parent2):
    def show(self):
        print(f"show all parent {self.name1} and {self.name2}")

child = Child()

child.show()
child.showParent1()
child.showParent2()

print(f"first parent is {child.name1}")
print(f"second parent is {child.name2}")