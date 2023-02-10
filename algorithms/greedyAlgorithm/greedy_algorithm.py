# Жадный алгоритм

"""
Жадные алгоритмы очень быстрые. Намного быстрее, чем две другие альтернативы
(Разделяй и властвуй — Divide & Conquer, и Динамическое программирование 
Dynamic Programming).
Они популярные, потому что они быстрые.

Жадный алгоритм должен всегда отвечать на этот вопрос: Каков лучший выбор в этот момент времени?
"""


def get_money(price: int, money_nomenal: dict) -> dict:
    """Считает оптимальное кол-во купюр для формирования суммы
    Принимает некую сумму в виде целого числа и словарь с номеналами купюр.

    Возвращает минимально возможное кол-во купюр для формирования переданной суммы.
    """

    for i in money_nomenal.keys():
        while i <= price > 0:
            price -= i
            money_nomenal[i] += 1

    return {k: v for k, v in money_nomenal.items() if v > 0}


def main():
    price = int(input('Введите цену (integer): '))
    money_nomenal = {
        100: 0,
        50: 0,
        10: 0,
        5: 0,
        1: 0
    }

    number_of_banknotes = get_money(price, money_nomenal)
    for k, v in number_of_banknotes.items():
        print(f'Купюр номеналом {k} - {v} шт.')


if __name__ == '__main__':
    main()

