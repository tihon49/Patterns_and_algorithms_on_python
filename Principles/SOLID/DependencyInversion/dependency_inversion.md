Принцип инверсии зависимостей гласит, что:

        Высокоуровневые модули не должны зависеть от низкоуровневых модулей. И то,
        и другое должно зависеть от абстракций.
        Абстракции не должны зависеть от деталей. Детали должны зависеть от
        абстракций.
        Принцип инверсии зависимостей направлен на уменьшение связи между классами
        путем создания слоя абстракции между ними.

Смотрите следующий пример:

```python
class FXConverter:
    def convert(self, from_currency, to_currency, amount):
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.2


class App:
    def start(self):
        converter = FXConverter()
        converter.convert('EUR', 'USD', 100)


if __name__ == '__main__':
    app = App()
    app.start()
```

В этом примере у нас есть два класса FXConverter и App.

Класс FXConverter использует API от воображаемой третьей стороны FX для
преобразования суммы из одной валюты в другую. Для простоты мы жестко
закодировали обменный курс как 1.2. На практике вам нужно будет сделать
вызов API, чтобы получить обменный курс.

Класс App имеет метод start() который использует экземпляр класса
FXconverter для преобразования 100 EUR в USD.

App представляет собой высокоуровневый модуль. Однако App сильно зависит
от класса FXConverter, который зависит от API FX.

<div class="wrapper">
    <img
        class="open_close" 
        src="../../../src/img/principles/SOLID/dependency_inversion.svg">
    </img>
</div>

В будущем, если API FX изменится, он сломает код. Кроме того, если вы
хотите использовать другой API, вам потребуется изменить класс App.

Чтобы предотвратить это, необходимо инвертировать зависимость, чтобы класс
FXConverter должен был адаптироваться к классу App.

Для этого необходимо определить интерфейс и сделать App зависимым от него,
а не от класса FXConverter. А затем вы меняете FXConverter в соответствии
с интерфейсом.

<div class="wrapper">
    <img
        class="open_close" 
        src="../../../src/img/principles/SOLID/dependency_inversion2.svg">
    </img>
</div>

Сначала определите абстрактный класс CurrencyConverter, который действует
как интерфейс. Класс CurrencyConverter имеет метод convert() который
должны реализовать все его подклассы:

```python
from abc import ABC


class CurrencyConverter(ABC):
    def convert(self, from_currency, to_currency, amount) -> float:
        pass
```

Во-вторых, переопределите класс FXConverter таким образом, чтобы он
наследовался от класса CurrencyConverter, и реализуйте метод convert():

```python
class FXConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print('Converting currency using FX API')
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.2
```

В-третьих, добавьте метод __init__ в класс App и инициализируйте объект
CurrencyConverter:

```python
class App:
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter

    def start(self):
        self.converter.convert('EUR', 'USD', 100)
```

Теперь класс App зависит от интерфейса CurrencyConverter, а не от класса
FXConverter.

При следующем примере создается экземпляр FXConverter и передается в App:

```python
if __name__ == '__main__':
    converter = FXConverter()
    app = App(converter)
    app.start()
```

Результат:

        Converting currency using FX API
        100 EUR = 120.0 USD

<br>

---

<br>


В будущем можно будет поддерживать другой API конвертера валют путем
подкласса CurrencyConverter. Например, ниже определяется класс
AlphaConverter, наследуемый от CurrencyConverter.

<div class="wrapper">
    <img
        class="open_close" 
        src="../../../src/img/principles/SOLID/dependency_inversion3.svg">
    </img>
</div>

```python
class AlphaConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print('Converting currency using Alpha API')
        print(f'{amount} {from_currency} = {amount * 1.15} {to_currency}')
        return amount * 1.15
```

Поскольку класс AlphaConvert наследуется от класса CurrencyConverter, его
объект можно использовать в классе App без изменения класса App:

```python
if __name__ == '__main__':
    converter = AlphaConverter()
    app = App(converter)
    app.start()
```

Результат:

        Converting currency using Alpha API
        100 EUR = 114.99999999999999 USD


Собирем все вместе:

```python
from abc import ABC


class CurrencyConverter(ABC):
    def convert(self, from_currency, to_currency, amount) -> float:
        pass


class FXConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print('Converting currency using FX API')
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.2


class AlphaConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print('Converting currency using Alpha API')
        print(f'{amount} {from_currency} = {amount * 1.15} {to_currency}')
        return amount * 1.15


class App:
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter

    def start(self):
        self.converter.convert('EUR', 'USD', 100)


if __name__ == '__main__':
    converter = AlphaConverter()
    app = App(converter)
    app.start()

```


Вывод:

        Используйте принцип инверсии зависимостей, чтобы сделать код более
        надежным, сделав высокоуровневый модуль зависимым от абстракции, а
        не от конкретной реализации.


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

