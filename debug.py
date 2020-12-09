import datetime
import pickle


def get_array():
    with open('data.pkl', 'rb') as file:
        return pickle.load(file)


def merge(left_arr, right_arr):
    i = 0
    j = 0
    len_left = len(left_arr)
    len_right = len(right_arr)
    result = []
    while i < len_left and j < len_right:
        left = left_arr[i]
        right = int(right_arr[j])
        if int(left_arr[i]) < right:  # Номер элемента 773214; Элемент на котором ломается функция left_arr[i] = '63'
            result.append(left)
            i += 1
        else:
            result.append(right)
            j += 1
    result.extend(left_arr[i:])
    result.extend(right_arr[j:])
    return result


def merge_sort(array):
    e = len(array)
    s = 0
    if (e - s) > 1:
        medium = int((s + e) / 2)
        left_arr = merge_sort(array[s:medium])
        right_arr = merge_sort(array[medium:e])
        return merge(left_arr, right_arr)
    return array


def run(func, array):
    start = datetime.datetime.now()
    print('=' * 20, f' START {func} ', '=' * 20)
    print('START: ', start)
    print('first 50 sorted words:', func(array[:])[:50])
    finish = datetime.datetime.now()
    print('FINISH: ', finish)
    print('RESULT: ', finish - start)


if __name__ == '__main__':
    arr = get_array()
    run(merge_sort, arr)
