# Discussion about how to make a relation btn two objects instantiation
# of different classes

# Class Robot
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

# Class Person
class Person:
    def __init__(self, n, p, i, r):
        self.name = n
        self.personality = p
        self.is_setting = i
        self.robot = r

    def sit_down(self):
        self.is_setting = True

    def stand_up(self):
        self.is_setting = False

robot = Robot("Tom", "Red", 30)
person = Person("Adam", "Aggressive", False, robot)  # One way of passing an object

person.robot_owner = robot    # Another way of classes relations
person.robot_owner.IntroduceSelf()

