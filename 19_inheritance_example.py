class Animal:
    def __init__(self, color, weight, age):
        self.legs = 4
        self.color = color
        self.weight = weight
        self.age = age

    def info(self):
        print(
            "legs =", self.legs,
            "color =", self.color,
            "weight =", self.weight,
            "age =", self.age
        )


class Dog (Animal):
    def __init__(self, color, weight, age, breed):
        Animal.__init__(self, color, weight, age)
        self.breed = breed

    # polymorphism - overriding (changing the definition of the function after inheriting)
    def info(self):
        print("breed =", self.breed)
        print("This function is changed in the Dog class")


class Cat (Animal):
    def __init__(self, color, weight, age, foodhabit):
        Animal.__init__(self, color, weight, age)
        self.foodhabit = foodhabit


# d = Dog("White", "8 Kgs", "2 Years", "Alsatian")
# c = Cat("Black", "3 Kgs", "3 years", "Mouse")
#
# d.info()
# c.info()