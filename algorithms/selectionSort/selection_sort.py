"""
Selection sort (сортировка выбором)

Суть алгоритма заключается в проходе по массиву от начала до конца в поиске минимального
элемента массива и перемещении его в начало.

сложность O(n^2)
"""


lst_to_sort = [4, 2, 3, 6, 9, 0, 7, 1, 5, 8]


def selection_sort(lst: list) -> list:
    lst_lenght = len(lst)

    for i in range(lst_lenght - 1):
        min_index = i

        for j in range(i+1, lst_lenght):
            if lst[j] < lst[min_index]:
                min_index = j

        if min_index != i:
            lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst


sorted_list = selection_sort(lst_to_sort)
print(sorted_list)

