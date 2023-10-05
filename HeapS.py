def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[i] < arr[left_child]:
        largest = left_child

    if right_child < n and arr[largest] < arr[right_child]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    # Строим maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Прокидываем наибольшый элемент в конец
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Пример использования
arr = [12, 11, 13, 5, 6, 7]
heapsort(arr)
print("Отсортированный массив:", arr)
