# родительский, суперкласс
class Car:
    # ининциализатор
    def __init__(self,  model, color):
        self.model = model
        self.color = color
        self.speed = 0

    def drive_to(self, destination):
        print(f"Car {self.model} Driving to", destination)


# дочерний, подклас
class Bus(Car):
    def __init__(self, model, color, number):
        super().__init__(model, color)
        self.number = number

class Truck(Car):
    def drive_to(self, destination):
        print('Truck driving to', destination)


bus_42 = Bus("Mercedes", "red", 42)
truck = Truck('MAN', 'white')
car_subaru = Car('subaru', 'red')
vehicles = (bus_42, truck, car_subaru)
for v in vehicles:
    v.drive_to('Bishkek')


