class Vehicle:
    def start(self):
        print("Vehicle starting")


class Car(Vehicle):
    def start(self):
        super().start()
        print("Car starting")


class ElectricCar(Car):
    def start(self):
        super().start()


class Tesla(ElectricCar, Car):
    def start(self):
        super().start()
        print("Tesla ready")


Tesla_car = Tesla()
Tesla_car.start()


