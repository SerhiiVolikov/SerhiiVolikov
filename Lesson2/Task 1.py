weight = input("Please enter your weight in kilo:\n")
height = input("Please enter your height in centimeters:\n")
weight_1 = int(weight) * 10000
height_1 = int(height)
BMI = weight_1 / (height_1 * height_1)
lower_bound = 18.5
upper_bound = 25

print(f"My Body mass index = {BMI}")
if BMI < lower_bound:
    print("Your BMI is less than normal")
elif BMI > upper_bound:
    print("Your BMI is greater than normal")
else:
    print("Your BMI is normal")
