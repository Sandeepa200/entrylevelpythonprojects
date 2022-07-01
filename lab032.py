
marks_list = []
#All error handling with calculations

def average(x):
    try:
        return (sum(x)/len(x))
    except ZeroDivisionError:
        return 0

def maximum(y):
    if (len(y) > 0):
        return (max(y))
    else:
        return 0

def minimum(z):
    if (len(z) > 0):
        return (min(z))
    else:
        return 0

#report printing

def marks_report():
    print("Total cost: ", sum(marks_list))
    print("Average marks: ", average(marks_list))
    print("Highest mark: ", maximum(marks_list))
    print("Lowest mark: ", minimum(marks_list))


while True:
    mark = input("Enter a mark, 0 to 100: ")
    # check for "end" befor converting mark to float
    if (mark == "end"):
        marks_report()
        break
    # filtering for correct inputs
    try:
        real_mark = float(mark)
        if(real_mark < 0 ):
            print("Prices must be positive!")
        elif(real_mark > 100):
            print("That's not a valid mark!")
        else:
            # adding marks to list
            marks_list.append(real_mark)   
    except ValueError:
        #checking input is string or other
        print("This is not a number!")

