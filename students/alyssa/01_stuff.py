
import random  # Lets us generate random numbers.

n = 10  # Sets how many numbers the list will contain.

numbers = []  # Starts with an empty list.

for _ in range(n):  # Repeats n times.
    number = random.randint(1, 100)  # Picks a random integer from 1 to 100.
    numbers.append(number)  # Adds that integer to the list.

print("Array:", numbers)  # Prints the list.
print("Size:", len(numbers))  # Prints how many items are in the list.