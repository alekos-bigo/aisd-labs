import timeit


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


# Пример использования
my_list = [3, 6, 8, 10, 1, 2, 1]
# sorted_list = quicksort(my_list)
execution_time = timeit.timeit(lambda: quicksort(my_list.copy()), number=1000)
# print(sorted_list)
print(f"Время выполнения сортировки расчёской: {execution_time} секунд")
