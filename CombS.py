import timeit


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


my_list = [3, 6, 8, 10, 1, 2, 1]
execution_time = timeit.timeit(lambda: comb_sort(my_list.copy()), number=1000)
print(f"Время выполнения сортировки расчёской: {execution_time} секунд")

