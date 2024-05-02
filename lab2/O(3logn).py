def bin_search(arr, n):
    l, r = 0, len(arr) - 1

    while l <= r:
        m = l + (r - l) // 2
        if arr[m] == n:
            return True
        elif arr[m] < n:
            l = m + 1
        else:
            r = m - 1

    return False


def search_in_three_arrays(arr1, arr2, arr3, n):
    return bin_search(arr1, n) and bin_search(arr2, n) and bin_search(arr3, n)


arr1 = [int(i) for i in input('Введите первый отсортированный массив\n').split()]
arr2 = [int(i) for i in input('Введите второй отсортированный массив\n').split()]
arr3 = [int(i) for i in input('Введите третий отсортированный массив\n').split()]
n = int(input('Введите число\n'))

if search_in_three_arrays(arr1, arr2, arr3, n):
    print(f"Число {n} найдено в каждом массиве.")
else:
    print(f"Число {n} не найдено в каком-то массиве.")
