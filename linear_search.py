def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

numbers = [5, 2, 9, 1, 7]

target = int(input("Enter a number to search for: "))

result = linear_search(numbers, target)

if result != -1:
    print(f"Found {target} at index {result}")
else:
    print(f"{target} was not found in the list.")