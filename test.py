# Перемножить все не чётные значения в диапазоне от 0 до 9435
even = 0
a = 9436
while a > 0:
    if a % 2 == 0:
        even += 1
        print(even)
    if a % 2 != 0:
        break


