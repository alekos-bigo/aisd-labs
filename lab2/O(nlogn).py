def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Разделим массив на две половины
    mid = len(arr) // 2
    l_half = arr[:mid]
    r_half = arr[mid:]

    # Рекурсивно отсортируем обе половины
    l_half = merge_sort(l_half)
    r_half = merge_sort(r_half)

    # Объединим отсортированные половины
    return merge(l_half, r_half)


def merge(left, right):
    res = []
    l_i, r_i = 0, 0

    while l_i < len(left) and r_i < len(right):
        if left[l_i] < right[r_i]:
            res.append(left[l_i])
            l_i += 1
        else:
            res.append(right[r_i])
            r_i += 1

    # Добавим оставшиеся элементы, если такие есть
    res.extend(left[l_i:])
    res.extend(right[r_i:])

    return res


in_data = [int(i) for i in input('Введите массив чисел\n').split()]
sorted_data = merge_sort(in_data)
print(sorted_data)
