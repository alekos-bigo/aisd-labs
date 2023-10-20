import timeit
import random

def comb_sort(arr):
    gap = len(arr)
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True

        i = 0
        while i + gap < len(arr):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
            i += 1



my_list = [random.randint(1, 10000) for _ in range(10**4)]
comb_sort(my_list)
print("Отсортированный массив:")
print(*my_list)
execution_time = timeit.timeit(lambda: comb_sort(my_list.copy()), number=100)
# print(sorted_list)
print(f"Время выполнения сортировки рассчёской: \n{execution_time} секунд")
