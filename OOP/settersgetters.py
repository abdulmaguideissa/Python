# Exploring setters and getters in python

class Employee:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def email(self):
        return '{}.{}@corp.com'.format(self.firstname, self.lastname)

    @property
    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    @fullname.setter
    def fullname(self, name):
        firstname, lastname = name.split(' ')
        self.firstname = firstname
        self.lastname = lastname

    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.firstname = None
        self.lastname = None


employee1 = Employee('Sam', 'Harris')     # Using constructor

employee1.fullname = 'adam eissa'         # Using setters
print(employee1.firstname)
print(employee1.email)
print(employee1.fullname)

del employee1.fullname
