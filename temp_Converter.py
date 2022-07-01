
temp = input("Enter your Celsius temperture (eg: 10) : ")

if (temp.isdigit()):
    F = int((9*int(temp))/5 + 32)
    print("Your temperature in Fahrenheit is : ",F)
else:
    print("please enter only numbers")

