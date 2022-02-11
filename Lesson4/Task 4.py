print("Insert your expression: "), input()
answer = int(input("The answer will be: "))
print("Lets check")
expression = input('Insert mathematical expression: ')
print(("Will be:"), eval(expression))
while answer != (eval(expression)):
    print("You're wrong, try again: ")
    answer = int(input("The answer will be: "))
else:
    print("You're right ")
