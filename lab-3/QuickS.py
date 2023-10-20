import timeit
import random


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


# Пример использования
my_list = [random.randint(1, 10000) for _ in range(10**4)]
sorted_list = quicksort(my_list)
print("Отсортированный массив:")
print(*sorted_list)
execution_time = timeit.timeit(lambda: quicksort(my_list.copy()), number=100)
# print(sorted_list)
print(f"Время выполнения быстрой сортировки: \n{execution_time} секунд")
