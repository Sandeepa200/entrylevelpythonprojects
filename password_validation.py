import re

capital = re.compile("[A-Z]+")
simple = re.compile("[a-z]+")
numbers = re.compile("[0-9]+")
characters = re.compile("[#$@]+")

def psValidation (x):
    if (len(x)<6):
        print("Your password should have minimum 6 characters")
        psValidation(input ("Enter the password = "))
    elif(len(x)>16):
        print("Your password should have maximum 16 characters")
        psValidation(input ("Enter the password = "))
    elif(capital.search(x) is None):
        print("Your password should have at least 1 letter between [A-Z].")
        psValidation(input ("Enter the password = "))
    elif(simple.search(x) is None):
        print("Your password should have at least 1 letter between [a-z].")
        psValidation(input ("Enter the password = "))
    elif(numbers.search(x) is None):
        print("Your password should have at least 1 number between [0-9].")
        psValidation(input ("Enter the password = "))
    elif(characters.search(x) is None):
        print("Your password should have at least 1 character from [$#@].")
        psValidation(input ("Enter the password = "))
    else:
        print("Your password is acceptable")

psValidation(input ("Enter the password = "))