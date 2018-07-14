class Car:
    condition = "new"
    def __init__(self,model,color,mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
    
    def display_car(self):
        print("This is a {} {} with {} MPG.".format(self.color, self.model, self.mpg))

class ElectricCar(Car):

    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.battery_type = battery_type

    def drive_car(self):
        self.condition = "like new"

my_car = ElectricCar("DeLorean", "silver", "eightyeight", "moltensalt")


#Another example

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return "{}, {}, {}".format(self.x, self.y, self.z)

my_point = Point3D(1, 2, 3)
print(my_point)

