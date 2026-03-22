class Employee:
    name = "old employee"

    def showNewName(self):
        print(f"name = {self.name}")

    @classmethod
    def showRealName(cls):
        print(f"name = {cls.name}")

e = Employee()
e.name = "new name"

e.showNewName()
e.showRealName()