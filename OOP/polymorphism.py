# Inroducing polymorphism using python.
# Define a function in the superclass without implementation and
# raise error if it was not implemented.
# Implement this method in the subclasses.

# Superclass
class Person(object):
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

    def AddressGenerator(self):
        raise NotImplementedError("Subclass must implement this method")


# Subclass 1
class Engineer(Person):
    def __init__(self, salary):
        self.salary = salary
        super(Engineer, self).__init__("Adam", 55, 25)

    def GetSalary(self):
        return self.salary

    def AddressGenerator(self):
        return self.salary / 5

# Subclass 2
class Technician(Person):
    def __init__(self, craft):
        self.craft = craft
        super(Technician, self).__init__("Daemon", 21, 10)

    def GetCraft(self):
        return self.craft

    def AddressGenerator(self):
        return self.id / 2


engineer = Engineer(500)
print(engineer.GetSalary())
print(engineer.AddressGenerator())

techincian = Technician("Plumber")
print(techincian.AddressGenerator())