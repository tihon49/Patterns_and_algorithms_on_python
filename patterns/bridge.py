from abc import ABC, abstractmethod


"""
В данном примере паттерна МОСТ наследники класса Remote() (пульт) выступают в качестве интерфейсов,
а наследники класса Device() (устройство) выступают в качестве реализации.

Класс BaseDevice() сделан для реализации простых девайсов.
Классы Tv(), Radio() выступают в качестве конкретных реализаций, конечных устройств.
Класс AdvancedRemote() выступает в качестве расширенного интерфейса (пульта).
"""


class Device(ABC):
    """абстракция для устройств (реализаций)"""

    @abstractmethod
    def isEnabled(self):
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

    @abstractmethod
    def getVolume(self):
        pass

    @abstractmethod
    def setVolume(self):
        pass

    @abstractmethod
    def getChannel(self):
        pass

    @abstractmethod
    def setChannel(self):
        pass


class BaseDevice(Device):
    """базовая реализация, достаточная для большинства устройств"""

    def __init__(self):
        self.volumeLevel = 50
        self.channel = 1
        self.power = False

    def isEnabled(self):
        return self.power

    def enable(self):
        self.power = True

    def disable(self):
        self.power = False

    def getVolume(self):
        return self.volumeLevel

    def setVolume(self, value):
        if 0 <= value <= 100:
            self.volumeLevel = value

    def getChannel(self):
        return self.channel

    def setChannel(self, value):
        self.channel = value


class Remote():
    """класс интерфейс (пульт)"""

    def __init__(self, device: BaseDevice()):
        self.device = device

    def togglePower(self):
        if self.device.isEnabled():
            self.device.disable()
        else:
            self.device.enable()

    def volumeUp(self):
        self.device.setVolume(self.device.getVolume() + 1)

    def volumeDown(self):
        self.device.setVolume(self.device.getVolume() - 1)

    def channelUp(self):
        self.device.setChannel(self.device.getChannel() + 1)

    def channelDown(self):
        self.device.setChannel(self.device.getChannel() - 1)


class Tv(BaseDevice):
    """базовая реализация для устройства - телевизор"""
    pass


class Radio(BaseDevice):
    """базовая реализация для устройства - радио"""
    pass


def base_foo():
    """
    Демонстрация взаимодействия интерфейса и реализации
    """

    # создаём устройства (реализации)
    tv = Tv()
    radio = Radio()

    # создаём пульты для устройств (интерфейсы)
    tv_remote = Remote(tv)
    radio_remote = Remote(radio)

    # Tv
    print('Базовое состояние устройства Tv:')
    print('tv.power:', tv.power)
    print('tv.volumeLevel:', tv.volumeLevel)
    print('tv.channel:', tv.channel)
    print()

    tv_remote.togglePower()
    tv_remote.volumeDown()
    tv_remote.channelUp()

    print('Измененное состояние устройства Tv:')
    print('tv.power:', tv.power)
    print('tv.volumeLevel:', tv.volumeLevel)
    print('tv.channel:', tv.channel)
    print()

    ##### Radio ######
    print('Базовое состояние устройства Radio:')
    print('radio.power:', radio.power)
    print('radio.volumeLevel:', radio.volumeLevel)
    print('radio.channel:', radio.channel)
    print()

    radio_remote.togglePower()
    radio_remote.volumeUp()
    radio_remote.channelUp()

    print('Измененное состояние устройства Radio:')
    print('radio.power:', radio.power)
    print('radio.volumeLevel:', radio.volumeLevel)
    print('radio.channel:', radio.channel)
    print()


base_foo()

###########################РАСШИРЕННЫЙ ФУНКЦИОНАЛ################################

class AdvancedRemote(Remote):
    """Расширенный вариант пульта"""

    def mute(self):
        # установить уровень звука на ноль
        self.device.setVolume(0)


def advanced_foo():
    """
    Демонстрация взаимодействия расширенного интерфейса и реализации
    """

    # создаём устройство (реализацию)
    tv = Tv()

    # создаём расширенный пульт для устройства (интерфейс)
    tv_advanced_remote = AdvancedRemote(tv)

    print('#' * 20, 'РАСШИРЕННЫЙ ФУНКЦИОНАЛ' , '#' * 20)
    print('Базовое состояние устройства Tv:')
    print('tv.power:', tv.power)
    print('tv.volumeLevel:', tv.volumeLevel)
    print('tv.channel:', tv.channel)
    print()

    tv_advanced_remote.togglePower()
    tv_advanced_remote.volumeDown()
    tv_advanced_remote.channelUp()

    print('Измененное состояние устройства Tv:')
    print('tv.power:', tv.power)
    print('tv.volumeLevel:', tv.volumeLevel)
    print('tv.channel:', tv.channel)
    print()

    print('Теперь воспользуемся расширенным функционалом нового пульта:')
    tv_advanced_remote.mute()
    print('tv.volumeLevel:', tv.volumeLevel)


advanced_foo()
