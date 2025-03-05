# ------------------------------------------------------------
# Constants
# ------------------------------------------------------------
SIZE_SMALL = 1
SIZE_NORMAL = 2
STATE_CRACKED = 1
STATE_NORMAL = 2
TIPS_GREEN = 1
TIPS_YELLOW = 2
COLOUR_GREEN = 1
COLOUR_BROWN = 2
COLOUR_YELLOW = 3

# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
choice = ""
advice = ""
colour = 0
size = 0
state = 0
tips = 0

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
choice = input ("Would you like advice for a plant (Y/N)? ")
choice = choice.upper ()

# =====> Complete the condition to keep the loop going around
while (choice == "Y"):
    advice = ""

    colour = int (input ("What colour are the leaves (1) Green (2) Brown (3) Yellow: "))
    # =====> Complete the test condition to validate the colour
    if (colour < 1 or colour > 3):
        print ("Invalid leaf colour")
    else:
        size = int (input ("What size are the leaves (1) Small (2) Normal: "))
        # =====> Complete the test condition to validate the size
        if (size < 1 or size > 2):
            print ("Invalid leaf size")
        else:
            state = int (input ("What is the state of the leaves (1) Cracked or misshapen (2) Normal: "))
            # =====> Complete the test to validate the leaf state
            if (state == 1 or state == 2):
                tips = int (input ("What colour is the tips of the leaves (1) Green (2) Yellow: "))
                # =====> Complete the test to validate the tip colour
                if (tips == 1 or tips == 2):
                    # Have enough information to determine the type of fertilizer needed
                    # =====> Complete the test condition for nitrogen
                    if (colour == COLOUR_YELLOW):
                        advice = advice + " Nitrogen"
                    # =====> Complete the test condition for magnesium
                    if (tips == TIPS_YELLOW):
                        advice = advice + " Magnesium"
                    # =====> Complete the test condition for calcium
                    if (state == STATE_CRACKED):
                        advice = advice + " Calcium"

                    # =====> Complete the test condition for potassium
                    if (colour == COLOUR_BROWN and size == SIZE_NORMAL):
                        advice = advice + " Potassium"
                    # =====> Complete the test condition for phosphorous
                    elif (colour == COLOUR_BROWN and size == SIZE_SMALL):
                        advice = advice + " Phosphorous"
                else:
                    print("Invalid colour for tips of leaves")
            else:
                print ("Invalid leaf state")

    if (advice != ""):
        print (advice)
    else:
        print ("Nothing needed")

    # Ask if user wants to go again?
    choice = input("Would you like advice for a plant (Y/N)? ")
    choice = choice.upper()

print ("Goodbye")
