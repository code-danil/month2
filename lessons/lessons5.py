class Animal:
    def move(self):
        print('двигается')


class Swimming(Animal):
    def move(self):
        super().move()
        print('плавете')


class Flying(Animal):
    def move(self):
        super().move()
        print('летает')


class Duck(Flying, Swimming):
    def move(self):
        super().move()
        print('летает и плавет')


print(Duck.__mro__)
duck = Duck()
duck.move()

print('------')
print(Swimming.__mro__)
animal = Swimming()
animal.move()

