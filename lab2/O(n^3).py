def find_triplets_with_sum(arr, target_sum):
    n = len(arr)
    result = set()

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if arr[i] + arr[j] + arr[k] == target_sum:
                    triplet = sorted((arr[i], arr[j], arr[k]))
                    result.add(tuple(triplet))
    return result


arr = [int(i) for i in input('Введите массив чисел\n').split()]
target = int(input('Введите число\n'))
answer = find_triplets_with_sum(arr, target)
if len(answer) != 0:
    print(f'Все тройки чисел, сумма которых равна заданному числу:')
    for i in answer:
        print(i)
else:
    print(f'Нет ни одной тройки чисел, сумма которых равна заданному числу')
