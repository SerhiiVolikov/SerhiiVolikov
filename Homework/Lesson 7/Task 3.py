# Create a function called make_country, which takes in a country’s
# name and capital as parameters. Then create a dictionary from those two,
# with ‘name’ as a key and ‘capital’ as a parameter.
# Make the function print out the values of the dictionary
# to make sure that it works as intended.
from typing import List


def make_country(a, b):
    Capitals = dict()
    Capitals['Russia'] = 'Moscow'
    Capitals['Ukraine'] = 'Kiev'
    Capitals['USA'] = 'Washington'
    Countries: list[str] = ['Russia', 'France', 'USA', 'Russia']
    for country in Countries:
        if country in Capitals:
            print('The capital of ' + country + ' is ' + Capitals[country])
    else:
            print('The capital of ' + country + ' is unknown')


if __name__ == "__main__":
    print(make_country)
