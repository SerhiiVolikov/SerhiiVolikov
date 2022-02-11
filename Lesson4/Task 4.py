print("Insert your expression: ")
expression = input()
answer = int(input("The answer will be: "))
print("I need to check it"), (eval(expression))
while answer != (eval(expression)):
    print("You're wrong, try again: ")
    if answer != (eval(expression)):
        answer = int(input("Will be: "))
        print("You're wrong")
        print("Will be:", eval(expression))
        break
else:
    print("You are right.")
