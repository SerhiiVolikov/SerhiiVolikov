print("  UKRANIAN NUMBER VALID TEST")
phone_number = input("Please enter your phone number:\n")
number_length = 12
Ukraine_phone_code = "380"
#
if len(phone_number) == number_length:
    pass
else:
    raise SystemExit("Number is invalid")
if phone_number.isdecimal():
    pass
else:
    raise SystemExit("Number is invalid")
if phone_number[0:3] == Ukraine_phone_code:
    print("Numer is valid")
else:
    raise SystemExit("Number is invalid")
