# Асимптотика O(3n) означает, что мы должны использовать
# три алгоритма с асимптотикой O(n). O(n) - самый простой пример
# это проход по массиву. Тогда чтобы написать алгоритм
# с асимптотикой O(3n) придумаем алгоритм три раза проходящий
# по массиву и делающий при каждом проходе 1 действие.
# Пусть это будет алгоритм сравнивающий во сколько раз
# среднее квадратов чисел больше среднего чисел.

# Функция самого алгоритма, принимающая массив
def alg(arr):
    # Запоминаем длину массива
    n = len(arr)
    # Находим сумму всех элементов
    arrsum = array_sum(arr)
    # Возводим каждый элемент в квадрат
    arrsqr = array_sqr(arr)
    # Находим сумму элементов в квадрате
    arrsqrsum = array_sum(arrsqr)
    # Считаем среднее значение
    arravrg = arrsum/n
    arrsqravrg = arrsqrsum/n
    # Записываем в результат то, во сколько раз среднее квадратов
    # чисел больше среднего чисел
    result = arrsqravrg/arravrg

    return result


# Функция суммирования элементов массива
def array_sum(a):
    s = 0
    for i in a:
        s += i
    return s


# Функция возведения в квадрат элементов массива
def array_sqr(a):
    n = len(a)
    for i in range(n):
        a[i] = a[i]**2
    return a


# Пример использования алгоритма:
input_data = [int(i) for i in input('Введите числа через пробел\n').split()]
output_result = alg(input_data)
print(f'Среднее квадратов чисел больше среднего чисел в {output_result:.2f} раз')