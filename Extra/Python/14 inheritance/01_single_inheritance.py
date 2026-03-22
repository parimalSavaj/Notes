class Base:
    name = "base"
    def show(self):
        print(f"class is {self.name}")

class Child(Base):
    newName = "child"

    def showFullName(self):
        print(f"child class {self.name} + {self.newName}")

child = Child()
child.show()
child.showFullName()
print(child.name)
print(child.newName)