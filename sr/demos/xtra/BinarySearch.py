def find(numbers, number):
    start_index = 0
    end_index = len(numbers) - 1

    while end_index >= start_index:
        mid_index = (start_index + end_index) // 2
        if numbers[mid_index] == number:
            return mid_index
        elif number > numbers[mid_index]:
            start_index = mid_index + 1
        elif number < numbers[mid_index]:
            end_index = mid_index - 1
    else:
        return -1


def test_find(numbers, number):
    index = find(numbers, number)
    print(f"In {numbers} found {number} at index {index}")


test_find([], 3)
for number in [1, 2]:
    test_find([1], number)
for number in range(3, 8):
    test_find([4, 6], number)
for number in range(3, 10):
    test_find([4, 6, 8], number)
for number in range(3, 12):
    test_find([4, 6, 8, 10], number)
