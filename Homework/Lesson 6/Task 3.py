
list_1 = [i for i in range(1,11)]
list_2 = [number ** 2 for number in list_1]
result = tuple(zip(list_1,list_2))
print(result)
