from collections import UserDict

class Field:
    def __init__(self, value):
        if not self.__is_valid__(value):
            raise ValueError
        self.value = value

    def __str__(self):
        return str(self.value)

    def __is_valid__(self,value):
        return value == value       # useless

class Name(Field):
    # реалізація класу
    def __is_valid__(self,value):
        if len(value)>0:
            return True
        raise ValueError

class Phone(Field):
    # Реалізовано валідацію номера телефону (має бути перевірка на 10 цифр).

    def __is_valid__(self,value):
        if value.isdigit() and len(value) == 10:
            return True
        raise ValueError

    # реалізація класу
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
class Record:
    def __init__(self, name):
        if Name.__is_valid__(self, name):
            self.name = name
            self.phones = []

    # реалізація класу

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p for p in self.phones)}"

# Реалізовано зберігання об'єкта Name в окремому атрибуті.
# Реалізовано зберігання списку об'єктів Phone в окремому атрибуті.
    def add_phone(self, phone):
        if Phone.__is_valid__(self, phone):
            self.phones.append(phone)

    def remove_phone(self, phone):
        if Phone.__is_valid__(self, phone):
            for user_phone in self.phones:
                if user_phone == phone:
                    del self.phones[self.phones.index(user_phone)]

    def edit_phone(self, old_phone, new_phone):
#метод  edit_phone  має повертати  помилку, якщо телефон не знайдено.
        if Phone.__is_valid__(self, old_phone) and Phone.__is_valid__(self, new_phone):
            self.remove_phone(old_phone)
            self.add_phone(new_phone)
        else:
            raise ValueError

    def find_phone(self, phone):
#метод  find_phone  має повертати або об'єкт, або None. Ніяких рядків.
        if Phone.__is_valid__(self, phone):
            for user_phones in self.phones:
                if phone in self.phones:
                    #return self.phones[self.phones.index(phone)]
                    return self.phones
        return None

# --------------------
class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name] = record

    def find(self, name):
        if Name.__is_valid__(self, name):
            for user_name, record in self.data.items():
                if user_name == name:
                    return record
        return None

    def delete(self, name):
        if Name.__is_valid__(self, name):
            for user_name, record in self.data.items():
                if user_name == name:
                    del self.data[record.name]
                    break

