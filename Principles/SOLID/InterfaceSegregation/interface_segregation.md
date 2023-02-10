# Принцип разделения интерфейсов

        Интерфейс — это описание поведения, которое может выполнять объект. Например, когда вы нажимаете кнопку питания на пульте дистанционного управления телевизором, он включает телевизор, и вам не нужно заботиться о том, как это сделать.

        В объектно-ориентированном программировании интерфейс — это набор методов, которые объект должен иметь. Цель интерфейсов состоит в том, чтобы позволить клиентам запрашивать правильные методы объекта через его интерфейс.

## Пример принципа сегрегации интерфейса:

Рассмотрим следующий пример:

<div class="wrapper">
    <img
        class="open_close" 
        src="../../../src/img/principles/SOLID/Interface_Segregation_Principle.svg">
    </img>
</div>

Во-первых, определим абстрактный класс Vehicle, который имеет два
абстрактных метода: go() и fly():

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def fly(self):
        pass
```

Во-вторых, определитм класс Aircraft, который наследует класс Vehicle,
и реализуем методы go() и fly():

```python
class Aircraft(Vehicle):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")
```

В-третьих, определим класс Car, который наследует класс Vehicle.
Поскольку автомобиль не может летать, мы поднимаем исключение в
методе fly():

```python
class Car(Vehicle):
    def go(self):
        print("Going")

    def fly(self):
        raise Exception('The car cannot fly')
```

В этой конструкции класс Car должен реализовывать метод fly() из класса
Vehicle, который класс Car не использует.
Поэтому такая конструкция нарушает принцип сегрегации интерфейса.

Чтобы это исправить, нам нужно разделить класс Vehicle на более мелкие
(летающие и ездящие) и унаследовать эти классы в классах Aircraft и Car:

<div class="wrapper">
    <img
        class="open_close" 
        src="../../../src/img/principles/SOLID/Interface_Segregation_Principle2.svg">
    </img>
</div>

Во-первых, разделим интерфейс Vehicle на два меньших интерфейса:
Movable и Flyable, и наследуем класс Movable в классе Flyable:

```python
class Movable(ABC):
    @abstractmethod
    def go(self):
        pass


class Flyable(Movable):
    @abstractmethod
    def fly(self):
        pass
```

Во-вторых, наследум класс Flyable в классе Aircraft:

```python
class Aircraft(Flyable):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")
```

В-третьих, наследуем класс Movable в классе Car:

```python
class Car(Movable):
    def go(self):
        print("Going")
```

Вывод:

        Принцип разделения интерфейсов предполагает, что интерфейсы должны 
        быть небольшими с точки зрения сплоченности.
        Создавайте мелкозернистые интерфейсы, специфичные для клиента. 
        Клиенты не должны быть вынуждены реализовывать интерфейсы, которые 
        они не используют.




<style>
.wrapper {
    display: flex;
    padding: 20px;
    width: 400px;
    height: 300px;
    margin-bottom: 20px;
    background-color: white;
}

.open_close {
    background-color: white

}
</style>
