weight = 70
height = 1.85
BMI = weight / (height * height)
lower_bound = 18.5
upper_bound = 25



print("My Body mass index = ", end=str(BMI))
print("\n")




if BMI < lower_bound:
    print("Your BMI is normal: False")
if BMI > upper_bound:
    print("Your BMI is normal: False")
else:
    print("Your BMI is normal: True")

