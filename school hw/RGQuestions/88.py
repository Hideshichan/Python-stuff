# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
anotherRound = True
sandwich = ""
monthNumber = 0
axis = ""
userInput = ""

# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
def isValidSandwich (pSand):
    valid = False

    # =====> Complete the test for the length of a sandwich name
    if (len(pSand) >= 3) and (len(pSand) <= 20):
        valid = True

    return (valid)

def isValidMonth (pMonth):
    valid = False

    # =====> Complete the test for the month number
    if (((pMonth >= 1) and (pMonth <= 12))):
        valid = True

    return (valid)

def checkPresence ():
    choice = ""

    # =====> Complete the condition to keep looping if nothing typed
    while (choice == ""):
        choice = input ("Enter any key (nothing will keep asking): ")

def isValidAxis (pAxis):
    valid = False

    pAxis = pAxis.upper()
    # =====> Complete the condition to valid a 3-D axis label using
    #        a range check with only two bounds
    if (pAxis == "X" or pAxis == "Y" or pAxis == "Z"):
        valid = True

    return (valid)

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
while (anotherRound == True):
    sandwich = input ("Enter your favourite sandwich: ")
    if (isValidSandwich (sandwich)):
        print ("Good choice")
    else:
        print ("Invalid sandwich")

    monthNumber = int (input ("Enter the number of the month: "))
    if (not isValidMonth (monthNumber)):
        print ("Invalid month")
    else:
        print ("Valid month")

    checkPresence ()

    axis = input ("Enter a 3-D axis: ")
    if (isValidAxis (axis)):
        print ("Valid axis")
    else:
        print ("Invalid axis")

    userInput = input ("Another round (Y/N)")
    userInput = userInput.upper()

    # =====> Complete the test to keep looping as long as user
    #        enters upper- or lower-case letter 'Y'
    if (userInput != "Y" or userInput != "y"):
        anotherRound = False