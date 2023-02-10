"""
Insertion sort (сортировка вставками)

алгоритм сортирует массив по мере прохождения
по его элементам. На каждой итерации берется элемент и сравнивается с каждым элементом
в уже отсортированной части массива, таким образом находя «свое место», после чего элемент
вставляется на свою позицию. Так происходит до тех пор, пока алгоритм не пройдет по всему 
массиву. На выходе получим отсортированный массив.

Сложность данного алгоритма равна O(n^2).
"""


list_to_sort = [-3, 0, 5, 2, -8, 9, 7, 1]


def insertion_sort(lst: list) -> list:
    for index in range(1, len(lst)):
        current_value = lst[index]
        position = index

        while position > 0 and lst[position - 1] > current_value:
            lst[position], lst[position - 1] = lst[position - 1], lst[position]
            position -= 1

    return lst


result = insertion_sort(list_to_sort)
print(result)

# [-8, -3, 0, 1, 2, 5, 7, 9]
