# vehicle (color, capacity, mode)
# - aeroplane (company, flight_area)
#   - cargo aeroplane
#   - passenger aeroplane (permittedLuggage)
# - car
#   - small car
#   - large car


class vehicle:

    def __init__(self, color, capacity, mode):
        self.color = color
        self.capacity = capacity
        self.mode = mode


class aeroplane(vehicle):

    def __init__(self, color, capacity, company, flight_area):
        vehicle.__init__(self, color, capacity, 'air')
        self.company = company
        self.flight_area = flight_area


class car(vehicle):

    def __init__(self, color, capacity, brand, seats):
        vehicle.__init__(self, color, capacity, 'road')
        self.brand = brand
        self.seats = seats


class cargoA(aeroplane):

    def __init__(self, company):
        aeroplane.__init__(self, "black", 0, company, "domestic")


    def info(self):
        print(self.company, self.color, self.flight_area, self.capacity, self.mode)


class passA(aeroplane):
    def __init__(self, company, capacity, permittedLuggage):
        aeroplane.__init__(self, "white", capacity, company, "international")
        self.permittedLuggage = permittedLuggage


    def info(self):
        print(self.company, self.color, self.flight_area, self.capacity, self.mode, self.permittedLuggage)



c = cargoA("Jet Airways")
p = passA("Indigo", "180", "7Kg")

c.info()
p.info()