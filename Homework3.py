class Person:
    def __init__(self, name, dob, occupation, higher_education):
        self.name = name
        self.__occupation = occupation  # приватный отрибут
        self.__higher_education = higher_education  # приватный отрибут
        self.dob = dob

    def introduce(self):
        print(f"Привет! Меня зовут: {self.name}я родился {self.dob} и я работаю как {self.occupation}. Высшее образование {self.higher_education}")

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

class Classmate(Person):
    def __init__(self, name, dob, occupation, higher_education, group_name):
        super().__init__(name, dob, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        super().introduce()
        print(f"Я учусь в группе: {self.group_name}")


class Friend(Person):
    def __init__(self, name, dob, occupation, higher_education, hobby):
        super().__init__(name, dob, occupation, higher_education)
        self.hobby = hobby


print('Информация о Person')
person1 = Person('Кирилл', '15.02.1999', 'Программист', True)
person1.introduce()

print('Информация о Classmate')
classmate1 = Classmate('Настя', '21.08.2000', 'дизайнер', True, 'группа 601')
classmate1.introduce()


print('Иноформация о Friend')
friend1 = Friend('Алиса', '12.05.2002', 'студент', False, 'Страна чудес')
friend1.introduce()

