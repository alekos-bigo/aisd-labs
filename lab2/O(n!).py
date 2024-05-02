def permutations(seq, curr_i=0):
    if curr_i == len(seq):
        print(tuple(seq))
        return
    for i in range(curr_i, len(seq)):
        # Меняем местами текущий элемент с элементом на текущем индексе
        seq[curr_i], seq[i] = seq[i], seq[curr_i]
        # Рекурсивно вызываем функцию для следующего элемента
        permutations(seq, curr_i + 1)
        # Возвращаем элементы на свои места для других перестановок
        seq[curr_i], seq[i] = seq[i], seq[curr_i]


my_sequence = [int(i) for i in input('Введите последовательность чисел\n').split()]
permutations(my_sequence)
