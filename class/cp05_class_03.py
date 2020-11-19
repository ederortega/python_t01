class Vehicle:
    def __init__(self, brand, model, year, max_speed):
        # object atribute
        self.brand = brand
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def start(self):
        print('Started')

    def stop(self):
        print('Stoped')


class Car(Vehicle):
    # class atribute
    STYLE_SEDAN = 'Sedan'
    STYLE_COUPE = 'Coupe'
    STYLE_HATCHBACK = 'Hatchback'

    def __init__(self, brand, model, year, max_speed, style):
        super().__init__(brand, model, year, max_speed)
        # object atribute
        self.style = style

    # str


stepway = Car('Renault', 'Stepway', 2020, 180, Car.STYLE_HATCHBACK)
print(stepway)

# class atributes


# dynamic attributes

# getattr

