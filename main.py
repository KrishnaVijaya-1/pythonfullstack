class Dog:
    attr1 = "mammal"
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))

x = Dog("x")
y = Dog("y")

x.speak()
y.speak()
