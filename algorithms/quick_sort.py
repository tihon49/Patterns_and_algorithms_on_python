# Quick sort
"""
Быстрая сортировка.

Суть:
    - берется рандомное значение из списка, которое становится 'опорным'    (reference_element).
    - все числа в списке, что меньше опорного, собираются в отдельный список (less).
    - все числа в списке, что равны опорному числу, собираются в отдельный список (middle) даже если такое число одно.
    - все числа в списке, что больше опорного, собираются в отдельный список (more).
    - далее списки less и more проходят этот же путь рекуосивно, и в конце концов возвращается 
      конкатенация списка less со списком middle и списком more, где все элементы отсортированы.
"""

import random


def qsort(lst):
    if len(lst) >= 2:
        reference_element = lst[random.randint(0, len(lst)-1)]
        less = list(filter(lambda x: x < reference_element, lst))
        middle = [i for i in lst if i == reference_element]
        more = list(filter(lambda x: x > reference_element, lst))
        
        return qsort(less) + middle + qsort(more)
    else:
        return lst


my_lst = [int(i) for i in input('Введите несколько целых чисел через пробел: ').split(' ')]
print(qsort(my_lst))
