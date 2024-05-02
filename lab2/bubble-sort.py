import random


def bubble_sort(array):
    swapped = True
    while swapped:
        swapped = False
        for index in range(len(array) - 1):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
                swapped = True


def main():
    array = [random.randint(-10, 10) for _ in range(10)]
    bubble_sort(array) # average - O(n^2)
    array.sort() # average - O(nlogn)
    print(array)


if __name__ == '__main__':
    main()
