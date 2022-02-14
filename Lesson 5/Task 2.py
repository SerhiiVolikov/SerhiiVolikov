# Exclusive common numbers.
#
# Generate 2 lists with the length of 10 with random integers from 1 to 10,
# and make a third list containing the common integers between the 2
# initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

import random

list_1 = (sorted(random.sample(range(100), 10)))
list_2 = (sorted(random.sample(range(100), 10)))
list_3 = []
print(" First list: ", list_1)
print(" Second list: ", list_2)
while list_1:
    temp = list_1.pop()
    list_3.append(temp)
while list_2:
    temp = list_2.pop()
    list_3.append(temp)
i = 1
while i < len(list_3):
    if list_3[i] in list_3[:i]:
        list_3.pop(i)
    else:
        i += 1

print(sorted(list_3))