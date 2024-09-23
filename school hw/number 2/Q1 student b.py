"""
btw answer to a) is smth like "prints the list then replaces a certain index with the given number"
PLEASE DONT COPY THIS INTO WHERE U PASTE CODE
"""


# ------------------------------------------------------------
# Import libraries
# ------------------------------------------------------------
import math

# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
myList = [1, 2, 3, 4, 5]
myNumber = 0
myLocation = -1
# =====> Create a variable named 'replacedValue' and set it to 0
replacedValue = 0
# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
# =====> Add parameters to the definition named 'pIndex', 'pList', 'pValue'
def replaceElement (pIndex, pList, pValue):
    # =====> Create a local variable named 'oldValue' and set it to 0
    oldValue = 0
    # =====> Replace the following line with an equivalent using the
    #        local variable 'oldValue', the input parameter 'pList', and
    #        the input parameter 'pIndex'
    oldValue = pList[pIndex]

    # =====> Replace the following line with an equivalent using the
    #        input parameters of 'pList', 'pIndex', and 'pValue'
    pList[pIndex] = pValue

    # =====> Return the value in the local variable 'oldValue'
    return oldValue
# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
print (myList)
myNumber = int (input ("Enter a new number: "))
myLocation = int (input ("Enter an index to replace: "))
# =====> Amend the call to the 'replaceElement()' subprogram to use
#        the input arguments of 'myList', 'myLocation', and 'myNumber'
#        Amend the line to store the returned value in the global
#        variable 'replacedNumber'
replacedValue = replaceElement (myLocation, myList, myNumber)
print (myList)
# =====> Add a line to print 'replacedValue' and 'myNumber'
print(f"The value {replacedValue} was replaced by {myNumber}")