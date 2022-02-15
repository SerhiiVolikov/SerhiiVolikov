# 1. Создайте список из элементов диапазона от 500 до 2500 с шагом 170, используя comprehensions.
# 2. Используя comprehensions, составьте список из квадратов каждого элемента в списке, если квадрат больше 50.
# 3. Cловарь состоит из транспортных средств и их массы в килограммах. Составьте список наименований транспортных средств массой менее 5000 кг.
# vehicles = {"Sedan": 1500, SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "bycicle": 7, "Motocycle": 100}
# compr1 = [i for i in range(500, 2500, 170)]
# print(compr1)

# cpmr2 = [i for i in range(15) if i**2 > 50]
# print(cpmr2)

vehicles = {"Sedan": 1500, SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "bycicle": 7, "Motocycle": 100}
cpmr3 = [key for key, values in vehicles.set if i < 5000]
print(cpmr3)