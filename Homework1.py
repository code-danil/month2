class Person:
    def __init__(self, name, birth_data, occupation, higher_education,):
        self.name = name
        self.brith_data = birth_data
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
     education_status = 'есть' if self.higher_education else 'нет'
     print(f'Привет! мкня зову: {self.name}. Я родился {self.brith_data} и работаю как {self.occupation} Высшее образование {education_status}.')


person1 = Person('Анастасия', '10.06.1990', 'менеджер', True)
person2 = Person('Богдан', '20.01.1985', 'радиомеханик', False)
person3 = Person('руслан', '05.09.2000', 'программист', True)

person1.introduce()
person2.introduce()
person3.introduce()

