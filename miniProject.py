# This is my fully complete programe for CAB SERVICE 
# In here I didn't use any 3rd party interface because teh question paper didn't mention it. So Have created it through terminal.
# I have used many queues for every sub category, because question says "vehicles shoud be in queue"
# I have pop the vehicles from queue in order to hire them or remove them.
# I have push the vehicle from queue in order to add them.
# I have push the poped vehicle to the queue in order to relese them.
# I haven't use price calculations and time calculations according to hires, Because question didn't mention about it.
# I have full filled all the mentions requiremnts as follows and programe can ask dynamic questions according to the user reqirements -
                                # Add a new vehicle to the system - line no.192
                                # Remove a vehicle from the system - line no.204
                                # Assign a job (hire) - line no.225
                                # Release form assigned job (hire) after completing - line no.236
                                # See available vehicles in each category - line no.215

categories = """
    Car:
    maximum number of passengers - 3 and 4
    AC/ Non AC

    Van:
    Maximum number of passengers - 6 and 8
    AC/ Non AC

    Three Wheelers:
    Maximum number of passengers - 3

    Trucks:
    Size - 7 ft and 12 ft

    Lorry:
    Max load and size - 2500kg and 3500kg
    """

# Queue implementation

class Queue:

    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        print(self.queue)

    # Display one by one queue
    def displayOne(self, index):
        return (self.queue[index])

    def size(self):
        return len(self.queue)

# I have created separate Queues for every vehicle Category and Sub Category then I have gave initial values for them

#car
C31 = Queue()
C32 = Queue()
C41 = Queue()
C42 = Queue()
# adding initial vehicle to queues
carList = [C31, C32, C41, C42]

for i in carList:
    i.enqueue("car01")
    i.enqueue("car02")
    i.enqueue("car03")

#van
V61 = Queue()
V62 = Queue()
V81 =Queue()
V82 = Queue()
# adding initial vehicle to queues
vanList = [V61, V62, V81, V82]

for i in vanList:
    i.enqueue("van01")
    i.enqueue("van02")
    i.enqueue("van03")

#threeveel
TV = Queue()
TV.enqueue("ThreeVeel01")
TV.enqueue("ThreeVeel02")
TV.enqueue("ThreeVeel03")

#truck
T7 = Queue()
T7.enqueue("Truck01")
T7.enqueue("Truck02")
T7.enqueue("Truck03")
T12 = Queue()
T12.enqueue("Truck01")
T12.enqueue("Truck02")
T12.enqueue("Truck03")

#lorry
L2 = Queue()
L2.enqueue("Lorry01")
L2.enqueue("Lorry02")
L2.enqueue("Lorry03")
L3 = Queue()
L3.enqueue("Lorry01")
L3.enqueue("Lorry02")
L3.enqueue("Lorry03")


# this part converting srting inputs to int the raise value error 
def input_validating():
    try:
        x = 0
        x = int(input("Enter a Number: "))
        return x
    except ValueError:
        print("Invalid input\n")

def user_requirement():
    print("What kind of Vehicle you want?\nThese are the Vehicle categories we have\n")
    print(categories)
    print("First of all, press the number which match with your desired Vehicle category \nCar - 1 \nVan - 2 \nThree Wheelers - 3 \nTrucks - 4 \nLorry - 5 \n")
    
    Vehicle = input_validating()

    if (Vehicle == 1 or Vehicle == 2):
        print("AC or Non AC? \n press 1 for AC vehicles or press 2 for Non AC vehicles\n")
        AC = input_validating()

        if Vehicle == 1:
            print(
                "Passanger count? \n press 1 for 3 passanger car or press 2 for 4 passanger car\n")
            passangers = input_validating()
            if passangers == 1:
                return "C3"+ str(AC)
            elif passangers == 2:
                return "C4"+ str(AC)
            else:
                print("your input is invalid please follow the guidelines!")

        elif Vehicle == 2:
            print(
                "Passanger count? \n press 1 for 6 passanger van or press 2 for 8 passanger van\n")
            passangers = input_validating()
            if passangers == 1:
                return "V6"+ str(AC)
            elif passangers == 2:
                return "V8"+ str(AC)
            else:
                print("your input is invalid please follow the guidelines!")
        else:
            print("your input is invalid please follow the guidelines!")

    elif Vehicle == 3:
        return "TV"

    elif Vehicle == 4:
        print("Truck Size? \n press 1 for 7ft Truck or press 2 for 12ft Truck\n")
        TSize = input_validating()
        if TSize == 1:
            return "T7"
        elif TSize == 2:
            return "T12"
        else:
            print("your input is invalid please follow the guidelines!")

    elif Vehicle == 5:
        print(
            "Max load and size? \n press 1 for 2500Kg Lorry or press 2 for 3500Kg Lorry\n")
        Load = input_validating()
        if Load == 1:
            return "L2"
        elif Load == 2:
            return "L3"
        else:
            print("your input is invalid please follow the guidelines!")

    else:
        print("your input is invalid please follow the guidelines!")

# in here I have used 2 same kind of lists because it raise errors if I use if z == i inside for loop

QList = [C31, C32, C41, C42, V61, V81, V62, V82, TV, T7, T12, L2, L3]
zList = ["C31", "C32", "C41", "C42", "V61", "V81", "V62", "V82", "TV", "T7", "T12", "L2", "L3"]
def addVehicle(z):
    x = input("Enter your new Vehicle Name: ")
    a = "Vehicle Succesfully added.\n"
    for i in zList:
        if z == i:
            index = zList.index(i)
            QList[index].enqueue(x)
            print(a)
            QList[index].display()
        else:
            continue

def removeVehicle(z):
    a = "Vehicle Succesfully Removed.\n"
    for i in zList:
        if z == i:
            index = zList.index(i)
            QList[index].dequeue()
            print(a)
            QList[index].display()
        else:
            continue

def displayVehicle(z):
    a = "These are the available vehicles.\n"
    for i in zList:
        if z == i:
            index = zList.index(i)
            print(a)
            QList[index].display()
        else:
            continue
# in here I have pop the hired vehicle from the queue then push the same vehicle after relesing it
def hireVehicle(z):
    print("\nThis is the next available vehicle to you according to the queue\n")
    for i in zList:
        if z == i:
            index = zList.index(i)
            vehicle = QList[index].displayOne(0)
            print(vehicle)
            start = input("\nDo you want to hire this Vehicle? (press 1 for yes 2 for No)\n")
            if start == "1":
                QList[index].dequeue()
                while True:
                    stop = input("You have hired the vehicle. press 1 after completing your journey\n")
                    if stop == "1":
                        QList[index].enqueue(vehicle)
                        print("You have stoped the hire.\nThank You!\n")
                        QList[index].display()
                        break
                    else:
                        continue
            else:
                break
        else:
            continue


# main code
print("Welcome to the NEW CAB SERVICE...\n")
print("Let us know what you are serching for...\n")

while True:
    print("\npress 1 to Add a new vehicle to the system \npress 2 to Remove a vehicle from the system \npress 3 to Assign a job (hire)\nPress 4 to see the available vehicles in each category \nPress 0 to exit\n")
    selection = input_validating()

    if selection == 1: #adding vehicle after getting user requirments
        z = user_requirement()
        addVehicle(z)
        continue
    elif selection == 2: #removing vehicle after getting user requirments
        z = user_requirement()
        removeVehicle(z)
        continue
    elif selection == 3: #hire and release vehicle after getting user requirments
        z = user_requirement()
        hireVehicle(z)
        continue
    elif selection == 4: #display vehicle after getting user requirments
        z = user_requirement()
        displayVehicle(z)
        continue
    elif selection == 0:
        break
    else:
        print("your input is invalid please follow the guidelines!")
