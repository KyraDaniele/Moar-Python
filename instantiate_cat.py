class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {}".format(self.name, self.age)

zelda = Cat("Zelda", 5)
stormy = Cat("Stormy", 3)

# print("{} is {}".format(zelda.name, zelda.age))
print(zelda.description())
print(stormy.description())