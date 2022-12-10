Selection sort (сортировка выбором)

    Суть алгоритма заключается в проходе по массиву от начала до конца в
    поиске минимального элемента массива и перемещении его в начало.

    сложность: O(n^2)


```python
lst_to_sort = [4,2,3,6,9,0,7,1,5,8]


def selection_sort(lst: list) -> list:
    lst_lenght = len(lst)

    for i in range(lst_lenght - 1):
        min = lst[i]
        index = i

        for j in range(i+1, lst_lenght):
            if min > lst[j]:
                min = lst[j]
                index = j

        if index != i:
            lst[i], lst[index] = lst[index], lst[i]

    return lst


sorted_list = selection_sort(lst_to_sort)
print(sorted_list)

```

### Пример:

![](../../src/gif/selection_sort.gif)
