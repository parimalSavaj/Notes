class Demo:
    name = "parimal"
    age = 18

    # constructor and so call dunder method
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

    def getInfo(self): # every type method want one argument self
        print(f"The name is {self.name} and age is {self.age} and language is {self.language}")

    @staticmethod
    def greet(): # if we create static method so don't want to pass self inside argument!
        print("good morning!")


demo = Demo("Parimal", 18, "JS")
# Demo.getInfo(demo) # above and this line both are same!!

demo.getInfo()