class Animal:

    is_alive = True
    
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry

    def description(self):
        print("{}".format(self.name))
        print("{}".format(self.age))  
        

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

zebra.description()

print(zebra.name, zebra.age, zebra.is_hungry, zebra.is_alive)
print(giraffe.name, giraffe.age, giraffe.is_hungry, giraffe.is_alive)
print(panda.name, panda.age, panda.is_hungry, panda.is_alive)

