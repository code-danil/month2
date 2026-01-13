class Contact:
    def __init__(self, name,   phone_number):
        self.name = name
        self.phone_number = phone_number

    def __str__(self):
        return f'Имя: {self.name}, Телефон: {self.phone_number}'

    @classmethod
    def validate_phone_number(cls, phone_number):
        if phone_number.isdigit() and len(phone_number) == 10:
            return True
        else:
            return False


class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            new_contact = Contact(name, phone_number)
            cls.all_contacts.append(new_contact)
            print(f'Контакт {name} Успешно добавлен')
        else:
            print('Ошибка: Неверный формат номера')


ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")
ContactList.add_contact("Тестовый Контакт", "123")

for contact in ContactList.all_contacts:
    print(contact)


