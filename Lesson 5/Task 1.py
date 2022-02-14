
import random

numbers = (sorted(random.sample(range(100), 10)))
print(numbers)
i = 0
max_value = numbers[i]
while i < len(numbers):
    if numbers[i] > max_value:
        max_value = numbers[i]
    i += 1
print("Max value is: ", max_value)
