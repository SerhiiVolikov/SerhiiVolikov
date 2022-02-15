import random

print("Please insert a word")
word = list(input())
i = 1
while i <= 5:
    i += 1
    print(random.sample(word, k=len(word)))
