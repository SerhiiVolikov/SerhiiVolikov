list_1 = (list(range(1, 101)))
ints = [int (item) for item in list_1]
print(ints)
i = 1
list_2 = []
q = [int(i) for i in list_2]
while i < len(ints):
    if i % 7 == 0 and i % 5 != 0:
        print(str(i))
        list_2.append(i)
    i += 1
print(list_2)
