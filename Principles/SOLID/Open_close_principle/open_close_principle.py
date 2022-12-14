# Допустим у нас есть класс Person

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'

    @classmethod
    def save(cls, person):
        print(f'Save the {person} to the database')


# Этот класс выполняет два функционала:
# 1) Управляет свойствами класса Person
# 2) Сохраняет пользователя в БД
# Что не соответствует  принципу единой ответственности


# Чтобы класс Person соответствовал принципу единой ответственности,
# необходимо создать другой класс, отвечающий за хранение Person в базе данных.
# Например:

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'


class PersonDB:
    def save(self, person):
        print(f'Save the {person} to the database')


person = Person('John Doe')
db = PersonDB()
db.save(person)

# Теперь код соответствует принципу единой ответственности:
# Класс Person отвечает за управление свойствами пользователя
# Класс PersonDB отвечает за хранение пользователя в базе данных
#
# Таким образом, если мы захотим поменять БД или что-то еще,
# нам не придется менять сам класс Person


##########################################################


# Чтобы сделать функционал удобнее, можно использовать шаблон фасада,
# чтобы класс Person был фасадом для класса PersonDB следующим образом: 

class PersonDB:
    def save(self, person):
        print(f'Save the {person} to the database')


class Person:
    def __init__(self, name):
        self.name = name
        self.db = PersonDB()    # <----

    def __repr__(self):
        return f'Person(name={self.name})'

    def save(self):
        self.db.save(person=self)

person = Person('John Smith')
person.save()
