# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
# =====> Write your code here
voltage = 0
# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
# =====> Write your code here
# Get the user input
voltage = int(input("Enter Voltage: "))
match voltage:
    case 1:
        print("Low voltage - opaque")
    case 2:
        print("Medium voltage - partially transparent")
    case 3:
        print("High voltage - fully transparent")
    case _:
        print("Invalid input")