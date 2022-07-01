def calculation(f,c,s):
    if (c == "+"):
        return f+s
    elif(c == "-"):
        return f-s
    elif(c == "*"):
        return f*s
    elif(c == "/"):
        if (f == 0.0 or s == 0.0):
            print("float division by zero")
            return "None"
        else:
            return f/s
    elif(c == "^"):
        return f**s
    else:
        return f%s

memory = []
def history(a):
    memory.append(a)

def memoryPrint():
    if (len(memory) == 0):
        print("No past calculations to show")
    for i in memory:
        print(i)

choices = ["+","-","/","*","^","%"]

def main():
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    print("8.History  : ? ")
    choice =input("Enter choice(+,-,*,/,^,%,#,$,?): ")
    if(choice == "#"):
        print(choice)
        print("Done. Terminating")
        exit()
    elif(choice == "$"):
        main()
    elif(choice == "?"):
        print(choice)
        memoryPrint()
        main()
    elif(choice not in choices):
        print("Unrecognized operation")
        main()
    elif(choice in choices):
        print(choice)
        f_num = input("Enter first number: ")
        print(f_num)
        if("$" in f_num):
            main()
        elif("#" in f_num):
            print("Done. Terminating")
            exit()
        s_num = input("Enter second number: ")
        print(s_num)
        if("$" in s_num):
            main()
        elif("#" in s_num):
            print("Done. Terminating")
            exit()
        answer = str(float(f_num)) +" "+ choice +" "+ str(float(s_num)) +" = "+ str(calculation(float(f_num),choice,float(s_num)))
        print(answer)
        history(answer)
        main()

while True:
    main()