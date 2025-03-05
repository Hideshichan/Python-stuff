# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
#           Username, Passcode, Favourite biscuit
userTable = [["AAA34", 4860, "chocolate bourbon"],
             ["CAB98", 7101, "custard cream"],
             ["GUS21", 5975, "rich tea"],
             ["RAT67", 4173, "chocolate digestive"],
             ["TUM83", 6462, "shortbread"],
             ["TXA84", 1435, "oatmeal raisin"]]

# =====> Write your code here
passcode = 0
# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
# =====> Write your code here
username = input("Enter your username: ")
while len(str(passcode)) != 4:
    passcode = int(input("Enter your passcode: "))
for user in userTable:
    if user[0] == username:
        if user[1] == passcode:
            biscuit = input("What is your favourite biscuit?")
            if biscuit == user[2]:
                print("Credentials accepted")
                break
            else:
                print("Incorrect biscuit")
                break
        else:
            print("Invalid passcode")
            break
    else:
        print("User not found")
        break