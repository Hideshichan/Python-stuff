import math # we need pi

option = 0
radius = 0.0 # Vars

def getUserOption ():
    validChoice = False
    userChoice = 0
    while (validChoice == False):
        showMenu()
        userChoice = int (input ("Enter an option: "))
        NUM_OPTIONS = 3
        if ((userChoice >= 1) and (userChoice <= NUM_OPTIONS)):
            validChoice = True
        else:
            print("Invalid option, try again")
    return (userChoice)

def showMenu ():
    AREA = "Area"
    CIRCUMFERENCE = "Circumference"
    EXIT = "Exit"
    print ("-"*35)
    print ("1 " + AREA)
    print ("2 " + CIRCUMFERENCE) # Main option menu
    print ("3 " + EXIT)


while (option != 3):
    option = getUserOption ()
    if (option == 1):
        radius = float (input ("Enter the radius of a circle: "))
        print ("The area is " + str (math.pi * radius ** 2)) # Calculates area
    elif (option == 2):
        radius = float (input ("Enter the radius of a circle: "))
        print ("The circumference is " + str (2 * math.pi * radius)) # where does math.pi come from (nvm found it)
print ("Goodbye")