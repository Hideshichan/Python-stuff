# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
userInput = "Ab123"
digits = ""
letters = ""

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
userInput = input ("Enter a 5 character key: ")

# Check the length, a-z, A-Z, 0-9
# =====> Check the length of the string
if (len(userInput)!= 5):
    print ("Invalid length")
# =====> Check for alphabetic and numeric characters
elif (not userInput.isalnum()):
    print ("Invalid character")
else:       # All good characters, split out the characters
    # =====> Set letters to the first two characters of the input
    letters = userInput[:2]
    # =====> Check for alphabetic characters only
    if (letters.isalpha() == False):
        print ("First two characters must be alphabetic")
    # =====> Check first letter to be upper case
    elif (not letters[0].isupper()):
        print ("First letter must be upper case")
    # =====> Check second letter to be lower case
    elif (not letters[1].islower()):
        print ("Second letter must be lower case")
    else:
        # Split out the digits
        # =====> Set digits to the last three characters
        digits = userInput[2:]
        # =====> Check all characters are digits
        if (digits.isdigit() == False):
            print ("Last three characters must be digits")
        else:
            print ("Well done.  Your entry is valid.")