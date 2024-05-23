def sub_arrays_with_simple_sum(array: list[int]) -> list[list[int]]:
    n = len(array)
    sub_arrays = []
    for start in range(n - 1):
        current_sum = 0
        for end in range(start, n):
            current_sum += array[end]
            if is_prime_number(current_sum):
                sub_arrays.append(array[start:end+1])

    return sub_arrays


def is_prime_number(number: int) -> bool:
    for divider in range(2, int(number ** 0.5) + 1):
        if number % divider == 0:
            return False

    return True


def main():
    test_arrays = [
        [1, 2, 3, 4, 5],
        [7, 10, 2, 3, 5],
        [4, 6, 8, 9, 11]
    ]
    for test_number, test_array in enumerate(test_arrays):
        print(f"Test: {test_number + 1}")
        for sub_array_number, sub_array in enumerate(sub_arrays_with_simple_sum(test_array)):
            print(f"Sub array number: {sub_array_number + 1}")
            print(f"Sub array: {sub_array}")
            print()
        print()


if __name__ == '__main__':
    main()
