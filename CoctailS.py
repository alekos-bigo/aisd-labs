def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while (swapped == True):
        # сбрасываем флаг swapped на каждой итерации,
        # чтобы проверить, нужно ли еще продолжать сортировку
        swapped = False

        # идем слева направо, как в обычной сортировке пузырьком
        for i in range(start, end):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # если не было перестановок, то массив уже отсортирован
        if (swapped == False):
            break

        # иначе, сбрасываем флаг swapped и двигаемся справа налево
        swapped = False
        end = end - 1

        # двигаемся справа налево, как в сортировке пузырьком
        for i in range(end - 1, start - 1, -1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # увеличиваем начальный индекс, так как самый маленький элемент
        # теперь находится в начале
        start = start + 1

# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
cocktail_sort(arr)
print("Отсортированный массив:", arr)

