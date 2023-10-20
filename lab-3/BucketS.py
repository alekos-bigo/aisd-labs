def bucket_sort(arr):
    # Находим минимальное и максимальное значение в массиве
    min_val = min(arr)
    max_val = max(arr)

    # Создаем пустые корзины
    bucket_range = (max_val - min_val) / len(arr)
    buckets = [[] for _ in range(len(arr) + 1)]
    # Распределяем элементы по корзинам
    for num in arr:
        index = int((num - min_val) / bucket_range)
        if index != len(arr):
            buckets[index].append(num)
        else:
            buckets[-1].append(num)
    # Сортируем каждую корзину и объединяем их
    sorted_arr = []
    for bucket in buckets:
        insertion_sort(bucket)  # Используем другой сортировочный метод (например, сортировку вставками)
        sorted_arr.extend(bucket)

    return sorted_arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Пример использования
if __name__ == "__main__":
    unsorted_array = [64, 25, 12, 22, 11]
    sorted_array = bucket_sort(unsorted_array)
    print("Отсортированный массив:")
    print(sorted_array)
