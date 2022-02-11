import random
# print("Please insert a word")
# word = int(input())
# print(word.random.randint())

# For list of integers
from numpy import character

items = input("Input comma separated sequence of words")
words = [character for character in items.split(",")]
print(",".join(sorted(list(set(words)))))
# import the random module
import random

# declare a list
sample_list = [1, 2, 3, 4, 5]

print("Original list : ")
print(sample_list)

# first shuffle
random.shuffle(sample_list)
print("\nAfter the first shuffle : ")
print(sample_list)

# second shuffle
random.shuffle(sample_list)
print("\nAfter the second shuffle : ")
print(sample_list)