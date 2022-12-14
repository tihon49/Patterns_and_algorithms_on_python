### Цель принципа open-closed состоит в том, чтобы упростить добавление новых функций (или вариантов использования) в систему без непосредственного изменения существующего кода.

<br>

### Рассмотрим следующий пример:

<div class="wrapper">
    <img 
        class="open_close" 
        src="../../../src/img/principles/SOLID/Open_closed_principle.svg">
    </img>
</div>

```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f'Person(name={self.name})'


class PersonStorage:
    def save_to_database(self, person):
        print(f'Save the {person} to database')

    def save_to_json(self, person):
        print(f'Save the {person} to a JSON file')


if __name__ == '__main__':
    person = Person('John Doe')
    storage = PersonStorage()
    storage.save_to_database(person)
```

В этом примере класс PersonStorage имеет два метода:

    1. Метод save_to_database() сохраняет пользователя в базе данных.
    2. Метод save_to_json() сохраняет пользователя в JSON-файл.

Позже, если требуется сохранить объект Person в XML-файл, необходимо
изменить класс PersonStorage. Это означает, что класс PersonStorage 
открыт не для расширения, а для модификации. Следовательно, это нарушает
принцип открытости-закрытости.

---
## Пример принципа «open-close»

Чтобы привести класс PersonStorage в соответствие с принципом open-close, необходимо спроектировать классы таким образом, чтобы при сохранении
объекта Person в другом формате файла, не требовалось его изменять.

Смотрим следующую схему классов:

<div class="wrapper">
    <img
        class="open_close" 
        src="../../../src/img/principles/SOLID/Open_closed_principle2.svg">
    </img>
</div>


```python
# Сначала определим абстрактный класс PersonStorage,
# содержащий абстрактный метод save()

from abc import ABC, abstractmethod

class PersonStorage(ABC):
    @abstractmethod
    def save(self, person):
        pass

# Во-вторых, создадим два класса PersonDB и PersonJSON,
# которые сохранят объект Person в базе данных и JSON-файле.
# Эти классы наследуются от класса PersonStorage

class PersonDB(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to database')


class PersonJSON(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to a JSON file')
```

Чтобы сохранить объект Person в XML-файл, можно определить новый класс
PersonXML, который наследуется от класса PersonStorage следующим образом:

<div class="wrapper">
    <img
        class="open_close" 
        src="../../../src/img/principles/SOLID/Open_closed_principle3.svg">
    </img>
</div>

```python
class PersonXML(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to a JSON file')
```

И вы можете сохранить объект Person в XML-файл с помощью класса PersonXML:

```python
if __name__ == '__main__':
    person = Person('John Doe')
    storage = PersonXML()
    storage.save(person)
```

---

## Сложим все это вместе:

```python
from abc import ABC, abstractmethod


class Person:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f'Person(name={self.name})'


class PersonStorage(ABC):
    @abstractmethod
    def save(self, person):
        pass


class PersonDB(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to database')


class PersonJSON(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to a JSON file')


class PersonXML(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to a XML file')


if __name__ == '__main__':
    person = Person('John Doe')
    storage = PersonXML()
    storage.save(person)
    storage = PersonJSON()
    storage.save(person)
```




<style>
.wrapper {
    display: flex;
    padding: 20px;
    width: 500px;
    height: 200px;
    margin-bottom: 20px;
    background-color: white;
}

.open_close {
    background-color: white

}
</style>