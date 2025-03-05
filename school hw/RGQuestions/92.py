# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
answer = "Y"
temp = 0

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------

# =====> Complete this line to check for looping condition
while (answer != "N"):
    # =====> Complete this line to accept a temperature from the user
    temp = int(input("Enter the temperature: "))

    # =====> Complete this line for checking if temperature is too hot
    if (temp > 30):
        print ("Too hot")
    # =====> Complete this line for checking if temperature is too cold
    elif (temp < 5):
        print ("Too cold")
    # =====> Complete this line for printing the correct message
    else:
        print ("Just right")

    answer = input ("Do you want to go again (Y, N)? ")
    answer = answer.upper ()

