
# З використанням циклу while та оператора розгалуження if (без використання range, for і т.д.) написати код,
# який обраховує суму всіх чисел, менших за 100, які діляться без залишку одночасно на 3 та 5.
# 5numbers = (1:100)
# number_max = 100
# while numbers <= 100:
#     print(numbers)
# if numbers % 3 and 5:
#
#     print(numbers)
#     numbers_sum += number
#     number += 1

surname = len(input())
faktorial = 1
i = 1
while i <= surname:
    faktorial *=  i
    i += 1
    print(faktorial)