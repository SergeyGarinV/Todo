### Домашнее задание Apple Task

Алгоритм быстрого поиска элемента
````
def get_fixed_point(array):
    midl = len(array) // 2
    index = midl
    while midl > 0:
        if midl % 2 and midl != 1:
            midl = midl // 2 + 1
        else:
            midl = midl // 2
        if array[index] > index:
            index -= midl
        elif array[index] < index:
            index += midl
        if array[index] == index:
            return index
    return False
