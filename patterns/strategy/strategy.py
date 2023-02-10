"""
Задача:

реализовать возможность вывода элементов списка:
    - FIFO
    - FILO
    - random

Помогает избежать логику с кучей if-ов, где вместо проверки входящего
алогоритма мы задаем необходимую стратегию.


Пример клиентской логики без паттерна стратегия:
def some_foo(self, lst: list, strategy='FIFO'):
    if strategy == 'FIFO':
        ...
    elif strategy == 'FILO':
        ...
    elif stretegy == 'random':
        ...

То же самое но с применением паттерна стратегия:
def some_foo(self, lst: list, strategy=AbstractStrategy):
    return strategy.get_list(lst)
"""

import random

from abc import ABC, abstractmethod


class IStrategy(ABC):
    """Абстрактный класс стратеги

    Args:
        ABC (_type_): _description_
    """
    @abstractmethod
    def get_list(self, lst: list) -> list:
        pass


class FIFO_Strategy(IStrategy):
    """Конкретная реализация стратегии """

    def get_list(self, lst: list) -> list:
        """Возвращает список таким какой он есть, без изменений"""
        lst_copy = lst.copy()
        return lst_copy


class FILO_Strategy(IStrategy):
    """Конкретная реализация стратегии """

    def get_list(self, lst: list) -> list:
        """Возвращает переданный список задом наперед"""
        lst_copy = lst.copy()
        lst_copy.reverse()
        return lst_copy


class Random_Strategy(IStrategy):
    """Конкретная реализация стратегии """

    def get_list(self, lst: list) -> list:
        """Возвращает переданный список в рандомном порядке"""
        lst_copy = lst.copy()
        random.shuffle(lst_copy)
        return lst_copy


class ListManager:
    """Какой-то класс для работы со списками
    
    Задача данного класса возвращать полученый список 
    согласно заданной стратегии:
        - FIFO
        - FILO
        - Random
    """
    def get_new_list(self, lst: list, strategy: IStrategy):
        return strategy.get_list(lst)


def main():
    # создали список
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # определили менеджера списков
    lst_manager = ListManager()

    # получим новый список задав стратегию: FILO
    filo_list = lst_manager.get_new_list(my_list, FILO_Strategy())
    print('FILO:\n', filo_list)

    # получим новый список задав стратегию: random
    random_list = lst_manager.get_new_list(my_list, Random_Strategy())
    print('RANDOM:\n', random_list)

    # получим новый список задав стратегию: FIFO
    fifo_list = lst_manager.get_new_list(my_list, FIFO_Strategy())
    print('FIFO:\n', fifo_list)

main()
