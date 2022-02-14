
list_1 = (list(range(1, 101)))
list_2 = []
ints = [int(item) for item in list_1]
print(ints)
i = 1
while i < len(ints):
    if i % 7 == 0 and i % 5 != 0:
        print(i)
    i += 1

for i in list_2:
    list_2.append(i)
    print(list_2)
