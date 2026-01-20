# родительский, суперкласс
class Car:
    # ининциализатор
    def __init__(self,  model, color):
        self.model = model
        self.color = color
        self.speed = 0

    def drive_to(self, destination):
        print(f"Car {self.model} Driving to", destination)

    def test(self):
        pass

# дочерний, подклас
class Bus(Car):
    def __init__(self, model, color, number):
        super().__init__(model, color)
        self.number = number

    def drive_to(self, destination):
        super().drive_to(destination)
        print(f"Bus {self.number} Driving to", destination)

bus_42 = Bus("Ikarus", "green", 42)
print(bus_42.number)
print(bus_42.speed)
bus_42.drive_to("Bishkek")
print(type(bus_42))
print(isinstance(bus_42, Bus))
print(isinstance(bus_42, Car))
print(type(bus_42))
if type(bus_42) == 'Bus':
    print("object is Bus")
