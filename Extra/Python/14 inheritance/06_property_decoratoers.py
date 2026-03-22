# A property decorator in Python (@property) is used to make a method behave like an attribute (variable), so you can access it without calling it like a function.

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == "":
            print("Name cannot be empty")
        else:
            self._name = value

# usage
p = Person("Parimal")
p.name = "John"     # calls setter
print(p.name)       # no () used