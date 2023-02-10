# Quick sort
"""
Быстрая сортировка.

Суть:
    - берется рандомное значение из списка, которое становится 'опорным'    (reference_element).
    - все числа в списке, что меньше опорного, собираются в отдельный список (less).
    - на случай, если чисел равных опорному несколько, создаётся список всех таких чисел, даже если такое число одно  (middle).
    - все числа в списке, что больше опорного, собираются в отдельный список (more).

    - далее списки less и more проходят этот же путь рекуосивно, и в конце концов возвращается 
      конкатенация списка less со списком middle и списком more, где все элементы отсортированы.
      result = [less] + [middle] + [more]
"""

import random


def qsort(lst):
    if len(lst) > 1:
        reference_element = lst[random.randint(0, len(lst) - 1)]
        less = [i for i in lst if i < reference_element]
        middle = [i for i in lst if i == reference_element]
        more = [i for i in lst if i > reference_element]

        return qsort(less) + middle + qsort(more)
    else:
        return lst


def main():
    my_lst = [
        int(i) for i in input("Введите несколько целых чисел через пробел: ").split(" ")
    ]
    print(qsort(my_lst))


if __name__ == "__main__":
    main()
