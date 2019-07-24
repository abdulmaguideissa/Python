# OOP using inheritance.
# A derived class inherits from a base class for the sake of generalization
# and object orientation design extention.

# Class Robot, the base class
class Robot(object):     # new style class
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

# Class Drone, the derived class
class Drone(Robot):    # Passing the superclass in the definition of the subclass
    def __init__(self, speed, weaponary, camera):
        self.speed = speed
        self.weaponary = weaponary
        self.camera = camera
        super(Drone, self).__init__("Dragon Fire", "black", 115)

    def DroneInfo(self):
        print "Speed is ", self.speed
        print("Weaponary is " + self.weaponary)
        print "Camera resolution is ", self.camera

machine = Drone(350, "1 inche machine gun", 200)
machine.cost = 200

machine.IntroduceSelf()
machine.DroneInfo()
