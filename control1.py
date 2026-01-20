class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self

    def set_age(self, age):
        self.__age = age

    def make_sound(self):
        print('Животные издает звуки.')

class Dog(Animal):
    def make_sound(self):
        print('Гав-гав')


class Cat(Animal):
    def make_sound(self):
        print('Мяу-мяу')


print('Тестирование классов')


dog = Dog('Бобик', 4)
cat = Cat('Том', 3)

print(f'{dog.get_name()} Говорит:')
dog.make_sound()
print(f'{dog.get_name()} Говорит:')
cat.make_sound()

print('Измненеие атрибутов')
dog.set_age(4)
cat.set_name('Том')

print('Теперь собаку зовут', dog.get_name(), dog.get_age(), 'ему лет')
print('Теперь кошку зовут', cat.get_name(), cat.get_age(), 'ему лет')