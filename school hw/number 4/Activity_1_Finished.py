# ------------------------------------------------------------
# Import libraries
# ------------------------------------------------------------
import random
import math
import time

# ------------------------------------------------------------
# Constants
# ------------------------------------------------------------
MAX_COUNT = 100             # Max number of items
PI = math.pi

# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
myList = []                 # To be filled with real numbers
mean = 0.0
abovePi = 0

# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
def genRandomReals (pList, pCount):
    number = 0.0

    # Complete the code to generate pCount number of random
    # real numbers (with decimals) and append each of them
    # to pList
    for i in range(pCount):
        pList.append(random.random() * 10)

# =====> Write the countAbovePi subprogram here.
#        It takes a list as a parameter and returns an integer.
def countAbovePi(pList):
    numberabovepi = 0
    for item in pList:
        if item > PI:
            numberabovepi += 1
    return numberabovepi

# =====> Write the findMean subprogram here.
#        It takes a list as a parameter and returns a real number.
def findMean(pList):
    total = 0
    for item in pList:
        total += item
    mean = total/len(pList)
    return mean

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
# =====> Add a message for thinking time and wait 1 second
print("Waiting 1 second")
time.sleep(1)
genRandomReals (myList, MAX_COUNT)
print (myList)

# =====> Add a message for thinking time and wait 1 second
print("Waiting 1 second")
time.sleep(1)
# =====> Call the countAbovePi subprogram and display result
abovePi = countAbovePi(myList)
print ("Above Pi: ", abovePi)

# =====> Add a message for thinking time and wait 1 second
print("Waiting 1 second")
time.sleep(1)
# =====> Call the findMean subprogram and display the result
mean = findMean(myList)
print ("Mean: ", mean)

print ("Goodbye")
