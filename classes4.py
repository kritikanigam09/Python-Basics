class Employee:
    def __init__(self, name):
        self.name = name
    
    def greet(self, other):
        print("Hello {}".format(other.name))

class CEO(Employee):
    def greet(self, other):
        print("Get back to work, {}!".format(other.name))

ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)
ceo.greet(emp)



