#--------------------------------------------------------------------
# Global variables
#--------------------------------------------------------------------
userInput = -1                      # Assume no user input
loopCount = 0                       # Outside loop termination

countScores = 0
total = 0
currentMax = 0
currentMin = 0

#--------------------------------------------------------------------
# Main program
#--------------------------------------------------------------------
loopCount = int (input ("How many different rounds? (0 to exit)) "))

# Just loop for the number of times inputted
# ===> Choose one line by removing the comment symbol
#while (loopCount != 0):
while (loopCount > 0):
    userInput = int (input ("Enter points scored (-1 to exit) "))

    countScores = 0
    total = 0

    # ===> Choose one line by removing the comment symbol
    currentMax = 0
    #currentMax = -1

    # ===> Choose one line by removing the comment symbol
    currentMin = 999
    #currentMin = 0

    # Keep looping as long as the user wants to
    # ===> Choose one line by removing the comment symbol
    #while (userInput == -1):
    while (userInput != -1):

        # Track items needed for calculating average
        countScores = countScores + 1
        total = total + userInput

        # Keep track of minimum and maximum values
        if (userInput > currentMax):
            currentMax = userInput
        if (userInput < currentMin):
            currentMin = userInput

        userInput = int (input ("Enter points scored (-1 to exit) "))

    # Print the statistics for this round
    print ("Max number: " + str (currentMax))
    print ("Min number: " + str (currentMin))

    # ===> Choose one line by removing the comment symbol
    #print ("Mean number: " + str (total // countScores))
    print ("Mean number: " + str (total / countScores))

    # Go back and do the outside loop again
    # ===> Choose one line by removing the comment symbol
    loopCount = loopCount - 1
    #loopCount = loopCount + 1