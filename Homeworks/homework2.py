class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def introduce(self):
        print(f"Привет! Меня зовут: {self.name} и я работаю как {self.occupation}.")

class Friend(Person):

    def __init__(self, name, occupation, hobby):
        super().__init__(name, occupation)
        self.hobby = hobby

    def introduce(self):
        print(f'Привет! Меня зовут: {self.name}, я работаю {self.occupation} а мое хобби - {self.hobby}')

class Classmate(Person):
    def __init__(self, name, occupation, group_name):
        super().__init__(name, occupation)
        self.group_name = group_name

    def introduce(self):
        print(f'Привет Меня зовут: {self.name}, я работаю {self.occupation}, я учусь в группе {self.group_name}')


friend1 = Friend('Максим', 'Доктор', 'Рыбалка')
friend2 = Friend('Анна', 'Дизайнер', 'рисование')
friend3 = Friend('Актилек', 'Учитель', 'шахматы')

classmate1 = Classmate('Руслан', 'Cтудент', 'Группа А')
classmate2 = Classmate('Катя', 'Студент', 'Группа Б')

print('Пример работы:')
classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()
friend3.introduce()

# Доп задание 1
person1 = Person('Андрей', 'Менеджер')
classmate1 = Classmate('Иван', 'Студент', 'Группа А')
friend1 = Friend('Мария', 'Инженер', 'спорт')
person2 = Person('Ольга', 'Врач')

people_list = [person1, classmate1, friend1, person2]

print('Выход списка людей')
for person_db in people_list:
    person_db.introduce()


# Доп задание 2
class BestFriend(Friend):
    def __init__(self, name, occupation, hobby, shared_memory):
        super().__init__(name, occupation, hobby)
        self.shared_memory = shared_memory

    def introduce(self):
        super().introduce()
        print(f'У нас есть общее воспоминание: {self.shared_memory}.')


print('Пример работы с BestFriend')
best_friend = BestFriend('Алиса', 'художница', 'Йога', 'Поездка в горы прошлым летом')
best_friend.introduce()

