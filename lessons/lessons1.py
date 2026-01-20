class Car:
    # Инициализатор
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def drive_to(self, destination):
        print(f"Car {self.model} Driving to", destination)

    def change_color(self, new_color):
        self.color = new_color


car_subaru = Car('Subaru', 'red')
car_subaru1 = Car('Subaru', 'red')
car_subaru2 = Car('Subaru', 'red')
car_kia = Car('Kia', 'silver')
print(car_subaru.model)
print(car_subaru.color)
print(car_kia.color)
print(car_kia.drive_to('Karakol'))
print(car_kia.change_color('black'))
car_subaru.model = 'Forster'
print(car_subaru.model)
car_subaru.max_speed = 140
# print(car_subaru.max_speed) Error
print(type(car_subaru))
print(type('dajfkdhf'))
