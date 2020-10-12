# a class is the complete TEMPLATE of what we want to make
# every class has 2 kind of things:
# - a set of attributes
# - a set of actions


# Human being
# attribs:  EyeColor, HairColor, SkinColor, Language, Height, Weight, Strength
# actions:  Walk, Run, Eat, Sit, Jump, Stand, See, Hear, Touch

# Allu Arjun
# attribs:  Black, Black, Fair, Telugu, 5.10, 65, High
#


class HumanBeing:

    def __init__(self, Name, Place, EyeColor, HairColor, SkinColor, Language, Height, Weight, Strength):
        self.Name = Name
        self.Place = Place
        self.EyeColor = EyeColor
        self.HairColor = HairColor
        self.SkinColor = SkinColor
        self.Language = Language
        self.Height = Height
        self.Weight = Weight
        self.Strength = Strength

    def Walk(self):
        print(self.Name, "is walking")

    def Run(self):
        print(self.Name, "is Running")

    def Eat(self):
        print(self.Name, "is Eating")

    def Sit(self):
        print(self.Name, "is Sitting")



h1 = HumanBeing("Allu Arjun", "Hyderabad", "Black", "Black", "Fair", "Telugu", 5.10, 65, "High")
h2 = HumanBeing("Shah Rukh Khan", "Mumbai", "Brown", "Black", "Fair", "Urdu", 5.8, 65, "Medium")

print(h1.Name)
print(h2.Name)

print(h1.Language)
print(h2.Language)


h2.Walk()
h1.Sit()

h3 = HumanBeing("Rajinikanth", "Chennai", "Black", "White", "Dark", ["Tamil", "Telugu"], 5.4, 75, "Less")
h3.Run()
print(h3.Language)

