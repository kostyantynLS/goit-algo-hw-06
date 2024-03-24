from collections import UserDict

class ExceptionWrongPhone(Exception):
    def __init__(self, number):
        self.number = number
        super().__init__(f"Неправильний номер телефону: {number}")

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    def name_string(self, name):
        return name

    def name_phone(self, phone):
        return phone

class Phone(Field):
    # Реалізовано валідацію номера телефону (має бути перевірка на 10 цифр).

    def validate_phone(self, phone_number):
            # Видаляємо всі символи, окрім цифр
            digits = ''.join(filter(str.isdigit, phone_number))
            # Перевіряємо, чи кількість цифр дорівнює 10
            if len(digits) != 10:
                raise ExceptionWrongPhone(self.number)
            else:
                return phone_number
        
    # реалізація класу
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"

# Реалізовано зберігання об'єкта Name в окремому атрибуті.
# Реалізовано зберігання списку об'єктів Phone в окремому атрибуті.
    def add_phone(self, phone):
        self.phones.append(Phone.validate_phone(self, phone))

    def remove_phone(self, phone):
        check_phone = Phone.validate_phone(self, phone)
        for user_phone in self.phones:
            if user_phone == check_phone:
                del self.phones[self.phones.index(user_phone)]

    def edit_phone(self, old_phone, new_phone):
        check_old = Phone.validate_phone(self, old_phone)
        check_new = Phone.validate_phone(self, new_phone)
        self.remove_phone(check_old)
        self.add_phone(check_new)

    def find_phone(self, phone):
        check_phone = Phone.validate_phone(self, phone)
        for user_phones in self.phones:
            if check_phone in self.phones:
                return self.phones[self.phones.index(phone)]
        return "not found"

# --------------------
class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name] = record

    def find(self, name):
        for user_name, record in self.data.items():
            if user_name.value == name:
                return record
        return None

    def delete(self, name):
        for user_name, record in self.data.items():
            if user_name.value == name:
                del self.data[record.name]
                break

