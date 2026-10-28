from sorting import data


def bubble_sort(numbers):
    # Work on a copy so the original list stays unchanged.
    result = numbers.copy()

    # Compare neighbors and swap them when they are out of order.
    for end in range(len(result) - 1, 0, -1):
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]

    return result


def selection_sort(numbers):
    # Work on a copy so the original list stays unchanged.
    result = numbers.copy()

    # Find the smallest remaining number and put it in the next position.
    for start in range(len(result)):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        result[start], result[smallest] = result[smallest], result[start]

    return result


def insertion_sort(numbers):
    # Work on a copy so the original list stays unchanged.
    result = numbers.copy()

    # Take each number and insert it into the correct place in the sorted part.
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current

    return result


if __name__ == "__main__":
    # The same Step 1 data is passed to all three algorithms.
    original = data.copy()

    print("Original list:", original)
    print("Bubble Sort:", bubble_sort(original))
    print("Selection Sort:", selection_sort(original))
    print("Insertion Sort:", insertion_sort(original))
