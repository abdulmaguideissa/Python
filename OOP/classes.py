# Introduction to OOP using python
class Robot:
    cost = 0
    def __init__(self, name, color, weight):  # Class Constructor, each instantiation will have its own values
        self.name = name
        self.color = color
        self.weight = weight

    def IntroduceSelf(self):
        print("My name is " + self.name)
        print("My color is " + self.color)
        print 'My weight is ', self.weight
        print 'My cost is ', self.cost, '$'

R1 = Robot("Tom", "Red", 50)      # Class instantiation
R1.cost = 2000
R1.IntroduceSelf()
